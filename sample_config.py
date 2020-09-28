import os

class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = os.environ.get("bc7f48d7-3c6f-4f32-aace-e33b12002d7e", "")
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("1120191019:AAFeKAeqNkaHpswK9_vjEqzMUNeL_wKvdZI", "")
    # The Telegram API things
    APP_ID = int(os.environ.get("1749924", 12345))
    API_HASH = os.environ.get("87e4a056bb574f7939ac283b9a9187ab")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = os.environ.get("984441749", "")
    # reg: Procedures
    UTUBE_BOT_USERS = AUTH_USERS
    SUPER_DLBOT_USERS = AUTH_USERS
    SUPER3X_DLBOT_USERS = AUTH_USERS
    SUPER7X_DLBOT_USERS = AUTH_USERS
    BANNED_USERS = os.environ.get("BANNED_USERS", "")
    # Wat was I thinking? :\
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 1572864000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # for storing the user details
    DB_SQLALCHEMY = "USERS.session"
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = os.environ.get("OUO_IO_API_KEY", "")
    #mirro
    MIRROR_ACE_API_KEY = os.environ.get("MIRROR_ACE_API_KEY", "")
    #mirror
    MIRROR_ACE_API_TOKEN = os.environ.get("MIRROR_ACE_API_TOKEN", "")
    # for Google Custom Search Engine
    GCS_API_KEY = os.environ.get("GCS_API_KEY", None)
    GCS_SE_ID = os.environ.get("GCS_SE_ID", None)
    # dict to hold the ReQuest queue
    ADL_BOT_RQ = {}
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # dict to hold Google Drive SignIns
    G_DRIVE_AUTH_DRQ = {}
