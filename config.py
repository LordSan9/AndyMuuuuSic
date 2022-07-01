from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = "9153121"
API_HASH = "6e4da67d7d29311511682ec7243b5140"
BOT_TOKEN = "5478849224:AAFOpQvBGYmTOIVNBhUcipIR8y4bdcSjMts"
SESSION_NAME = "AgCLqmEAjEq2zCVbLSUVDNojlWWuz8vn5k6JMbrlbVyyD1TGTHed3nCM3PcUzd0VfxLsBZggfVzTh8mHcS72l-Nmg7s9esjTSGogAqFvWhQmdLIrP29nHi-o8Sh89zO2FrI0PXwHGn0SLqSK20jXIGxtHRag0PrXigQ0EluCeNexAUziBGk5skJE3Zl_iX5Qs3IWLInkVIg7_WrmN9UVKolrfNxt2o6txHoaW155cJ20-mMWBy0JX2mZ9J66JWG7LDmwHljqSTZR9bMD9EegFECmqsqaPS8TA9dSQ1A8S13DkLgtTAdnZtUKJ0TpZMSKYeutqvmX_9qNfZaSjcnfoIMsUUu19gAAAAFG0Ct6AA"

# mandatory vars
OWNER_USERNAME = "IIlAndylII"
ALIVE_NAME = "Andy"
BOT_USERNAME = "x103x_bot"
UPSTREAM_REPO = "https://github.com/LordSan9/lMl10l"
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = "Z888I"
UPDATES_CHANNEL = "X_P13"

# database, decorators, handlers mandatory vars
MONGODB_URL = "mongodb+srv://ANDY:<password>@cluster0.hcjrr.mongodb.net/?retryWrites=true&w=majority"
COMMAND_PREFIXES = "!"
OWNER_ID = "5336448904"
SUDO_USERS = "5336448904"

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
