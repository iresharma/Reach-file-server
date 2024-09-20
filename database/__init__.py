import uuid
from os import environ
from urllib.parse import urlparse

from peewee import PostgresqlDatabase, Model, CharField, DoesNotExist, IntegrityError, ForeignKeyField


def extract_postgres_details(database_url):
    result = urlparse(database_url)

    # Extract the components
    user = result.username
    password = result.password
    host = result.hostname
    port = result.port
    dbname = result.path.lstrip('/')

    return {
        "host": host,
        "user": user,
        "dbname": dbname,
        "password": password,
        "port": port
    }


db_config = extract_postgres_details(environ.get('POSTGRES'))
db = PostgresqlDatabase(db_config["dbname"], user=db_config["user"], password=db_config["password"],
                        host=db_config["host"], port=db_config["port"])


class BaseModel(Model):
    class Meta:
        database = db


class Storage(BaseModel):
    id = CharField(unique=True, primary_key=True)
    user_account_id = CharField(unique=True)


class File(BaseModel):
    id = CharField(unique=True, primary_key=True)
    name = CharField()
    path = CharField(unique=True)
    size = CharField(null=True)
    lastModified = CharField()
    bucket_id = CharField()

class Iteration(BaseModel):
    id = CharField(unique=True, primary_key=True)
    name = CharField(unique=True)
    files = ForeignKeyField(File, backref="iteration")

db.connect()
db.create_tables([Storage, File])


def create_file(name, path, size, last_modified):
    try:
        file_id = str(uuid.uuid4())
        file = File.create(id=file_id, name=name, path=path, size=size, lastModified=last_modified)
        return file
    except IntegrityError as e:
        print(f"Error creating file: {e}")
        return None


def get_file(file_id):
    try:
        file = File.get(File.id == file_id)
        return file
    except DoesNotExist:
        print(f"File with id {file_id} does not exist.")
        return None


def update_file(file_id, name=None, path=None, size=None, last_modified=None):
    try:
        file = File.get(File.id == file_id)
        if name:
            file.name = name
        if path:
            file.path = path
        if size:
            file.size = size
        if last_modified:
            file.lastModified = last_modified
        file.save()
        return file
    except DoesNotExist:
        print(f"File with id {file_id} does not exist.")
        return None


def delete_file(file_id):
    try:
        file = File.get(File.id == file_id)
        file.delete_instance()
        return True
    except DoesNotExist:
        print(f"File with id {file_id} does not exist.")
        return False


def get_account_details(user_id: str):
    try:
        resp = db.execute_sql(f"select * from user_accounts where id = '{user_id}'")
        columns = [column[0] for column in resp.description]
        result_as_dict = [dict(zip(columns, row)) for row in resp.fetchall()]
        return result_as_dict[0]
    except Exception as e:
        print(e)
    return {}


def create_bucket(user_id: str):
    bucket_id = str(uuid.uuid4())
    try:
        Storage.create(id=bucket_id, user_account_id=user_id)
    except Exception as e:
        print(e)
    try:
        db.execute_sql(f"update user_accounts set bucket_id = '{bucket_id}' where id = '{user_id}'")
    except Exception as e:
        print(e)
    return bucket_id
