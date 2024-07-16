from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "26516344"))
    API_HASH = getenv("API_HASH", "7a3f7d55d89476a15a62b4dd39062556")
    BOT_TOKEN = getenv("BOT_TOKEN", "7335170758:AAGSbCQwm7BWSuVBsVryZ2f7feDavVPCDi8")
    FSUB = getenv("FSUB", "unb_info")
    CHID = int(getenv("CHID", "-1002065300634"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://gojosat192007:DUG8sM52Ojaodfow@cluster0.j52i2we.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
