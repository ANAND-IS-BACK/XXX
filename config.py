## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAC_2ATtcg_rByNIjr_Fl3d24mhMjFMC5hR8IWkwm_9g0lKIwK3hoNVTl2MOu9e3Pwd9oXT9ceNijMtL9CB0UCqjriAFir6LcAUYnA2xRblCai05efipuslXXtRFntsvcWvgsbfTSJ0VeUm-MONAEhQUjFKeeJ96DSHyryVNj4i3Kk0pl1Ah0yKQOIw-SPN93rKilpFDH8l9HQrPEQq2xB09csYLzGcit6pex8Gao6xBH9PK19sEslO20pV3y1_MX8mvAexT54V4CBDuFjAe305sdRJGYCdcVwnGGTCFmGYR58jt1sMM8p-wD4Ur01ncdqZcJL29mmT6OOeS-VNOkyBsAAAAAUlgwOIA")
BOT_TOKEN = getenv("BOT_TOKEN", "5509995800:AAFAhfJmhhkdnLaZHrYgSCyeRnJp6AXY794")
BOT_NAME = getenv("BOT_NAME", "INDIAN MUSIC")
API_ID = int(getenv("API_ID", "18076543"))
API_HASH = getenv("API_HASH", "f05b5c6a49b824b88c99e206a5c30d8c")
OWNER_NAME = getenv("OWNER_NAME", "𝐌𝐫.​𝐗")
OWNER_USERNAME = getenv("OWNER_USERNAME", "MR_X_OP_BOLTE")
ALIVE_NAME = getenv("ALIVE_NAME", "𝐌𝐫.​𝐗")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
