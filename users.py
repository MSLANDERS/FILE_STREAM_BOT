import sys
import os
import asyncio
from pyrogram.errors import *
from database.users_db import db
from pyrogram import Client, filters
from info import ADMINS

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

@Client.on_message(filters.private & filters.command("users") & filters.user(ADMINS))
async def users(bot, update):
    total_users = await db.total_users_count()
    text = "Bot Status\n"
    text += f"\nTotal Users: {total_users}"
    await update.reply_text(
        text=text,
        quote=True,
        disable_web_page_preview=True
    )

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

@Client.on_message(filters.private & filters.command(['restart']) & filters.user(ADMINS))
async def restart(client, message):
    msg = await message.reply_text(
        text="<i>Trying To Restarting.....</i>",
        quote=True
    )
    await asyncio.sleep(2)
    await msg.edit("<i>Server Restarted Successfully ✅</i>")
    os.execl(sys.executable, sys.executable, *sys.argv)

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP
