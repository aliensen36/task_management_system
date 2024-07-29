import os
from dotenv import load_dotenv

load_dotenv()


print(f"POSTGRES_DB: {os.getenv('POSTGRES_DB')}")