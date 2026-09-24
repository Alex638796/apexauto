import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "0"))
    API_HASH = os.environ.get("API_HASH", "")
    ADMIN_ID = int(os.environ.get("ADMIN_ID", "0"))
    DB_URL = os.environ.get("DB_URL", "")
    DB_NAME = os.environ.get("DB_NAME", "AppxBot")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "0")
    USERLINK = os.environ.get("USERLINK", "https://t.me/")
    TUTORIAL_VIDEO = os.environ.get("TUTORIAL_VIDEO", "https://t.me/")
