import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()
que = {}
admins = {}

#------------------------ Important Stuff 😌 -----------------------

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "500"))
STRING_SESSION = getenv("STRING_SESSION")
BOT_USERNAME = getenv("BOT_USERNAME")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1803475435 5411211921 539479731").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5065752827").split())
)  # Input type must be interger

#•••••••••••••••••••••••• Mongodb Url Stuff •••••••••••••••••••••••

MONGODB_URL = getenv("MONGODB_URL")

#________________________ Updates 🍃 & Music bot name_______________________________

NETWORK = getenv("NETWORK")
GROUP = getenv("GROUP")
BOT_NAME = getenv("BOT_NAME")

#************************* Image Stuff 💕 **************************

IMG_1 = getenv("IMG_1", "https://telegra.ph//file/252232ffc1e29f35cde27.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph//file/252232ffc1e29f35cde27.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph//file/a4920ccd56e4d4a09fd95.jpg") 
aiohttpsession = aiohttp.ClientSession()


