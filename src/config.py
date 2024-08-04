# Get data from .env

from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")
if not BOT_TOKEN:
    print("No token found!")
    exit(1)
