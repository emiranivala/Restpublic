# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23783378"))
API_HASH = getenv("API_HASH", "1151425ad8d6fa61d47247f9ee841a37")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "922270982").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "-1002364132130")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002362823742"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "20"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "50000000"))

#AutoDeleteTime
SECONDS = int(getenv("SECONDS", "300")) #5_minutes
