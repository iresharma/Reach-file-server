import os
from R2Wrapper import R2Wrapper

r2 = R2Wrapper(os.environ['ENDPOINT'], os.environ['KEY_ID'], os.environ['SECRET_KEY'], 'apac')
r2.list_bucket('temp-reach-bucket', '/')
# r2.init_bucket('123', {
#     'accountId': '123',
#     'name': 'Shreesh',
#     'email': 'sgkul2000@gmail.com'
# })