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
    api_id=24514748,
    api_hash="5dbe5df68358919d32cbfd341e0142f1",
    bot_token="8371213085:AAHhzJnVAIaRjbkJHGjIg0W6oRckTnWoyfk",
    plugins=dict(root="MZombie")
    )


with open('./config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)


sourse_dev = config['sourse_dev']


DEVS = []
DEVS.append(6334408675)
DEVS.append(6334408675)
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
