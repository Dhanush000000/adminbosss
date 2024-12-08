# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20389440"))
    API_HASH = getenv("API_HASH", "a1a06a18eb9153e9dbd447cfd5da2457")
    BOT_TOKEN = getenv("BOT_TOKEN", "7937281826:AAG060UidbGidTlghkPLJ5uAiWIC133zsG4")
    SESSION_STRING = getenv("SESSION_STRING", "")
    SUDO = list(map(int, getenv("SUDO", "5798247275 6739280140").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://adminboss143:adminboss143@cluster0.hp7lw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
