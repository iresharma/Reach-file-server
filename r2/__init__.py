import os
from R2Wrapper import R2Wrapper

if __name__ == '__main__':
    r2 = R2Wrapper(os.environ['ENDPOINT'], os.environ['KEY_ID'], os.environ['SECRET_KEY'], 'apac')
    r2.create_folder('temp-reach-bucket', '/wow')