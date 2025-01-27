import os

API_ID = os.environ.get("API_ID", "26148784")

API_HASH = os.environ.get("API_HASH", "e1428799c0aeccd0a3cd1f15606e7a80")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", "7148824590" ))

LOG = "2441473161",

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7148824590").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


