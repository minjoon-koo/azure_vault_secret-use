import os
from dotenv import load_dotenv
load_dotenv(".env")

print(os.environ["AUTH_PASSWORD"])