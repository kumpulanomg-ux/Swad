import json
from pyrogram import Client, idle
from pyromod import listen
from pyrogram.types import ChatPrivileges, ChatPermissions

#
#==================================================
#
#███████╗███████╗██████╗  ██████╗ 
#╚══███╔╝██╔════╝██╔══██╗██╔═══██╗
#  ███╔╝ █████╗  ██████╔╝██║   ██║
# ███╔╝  ██╔══╝  ██╔══██╗██║   ██║
#███████╗███████╗██║  ██║╚██████╔╝
#╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
#
#==================================================

bot = Client(
    "m4o",
    api_id=8186557,
    api_hash="efd77b34c69c164ce158037ff5a0d117",
    bot_token="8218017886:AAGvdiRCAHYEhuyuRZOwTJ8i8Jz6NaNw8Eo",
    plugins=dict(root="MZombie")
    )


with open('./config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)


sourse_dev = config['sourse_dev']


DEVS = []
DEVS.append(214997951)
DEVS.append(7654641648)
owner_id = sourse_dev
bot_id = bot.bot_token.split(":")[0]


async def start_zombiebot():
    await bot.start()
    for hh in DEVS:
        try:
            await bot.send_message(hh, f"**◍ تم تشغيل الصانع بنجاح 🚦\n√**")
        except:
            pass
    await idle()

#
#==================================================
#
#███████╗███████╗██████╗  ██████╗ 
#╚══███╔╝██╔════╝██╔══██╗██╔═══██╗
#  ███╔╝ █████╗  ██████╔╝██║   ██║
# ███╔╝  ██╔══╝  ██╔══██╗██║   ██║
#███████╗███████╗██║  ██║╚██████╔╝
#╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
#
#==================================================