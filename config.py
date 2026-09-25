import os
##Code Written By @ItsMeMaster
##Code Written By @ItsMeMaster

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    DB_NAME = os.environ.get("DB_NAME", "")
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    ADMIN_ID = int(os.environ.get("ADMIN_ID", "0"))
    DB_URL = os.environ.get("DB_URL", "")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "")  # Your Log Channel ID (Bot ko ADMIN BNAYE)
    USERLINK = os.environ.get("USERLINK", "")
    TUTORIAL_VIDEO = os.environ.get("TUTORIAL_VIDEO", "")
