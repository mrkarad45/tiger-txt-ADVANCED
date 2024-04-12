import os

API_ID = API_ID =21659643

API_HASH = os.environ.get("API_HASH", "c5f065905ef47e693b47e0f60bb67217")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7074952314:AAHWCX4U0RyMq4VIuS-ZgQA5oRo0pCdhKpQ")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6045786693))

LOG = -1002140760823

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


