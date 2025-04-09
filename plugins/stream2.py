import asyncio
import os
import random
from web.utils.file_properties import get_hash
from pyrogram import Client, filters, enums
from info import BIN_CHANNEL, BAN_CHNL, BANNED_CHANNELS, URL, CHANNEL, BOT_USERNAME
from utils import get_size
from Script import script
from database.users_db import db
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

#Dont Remove My Credit @MSLANDERS 
# For Any Kind Of Error Ask Us In Support Group @MSLANDERS_HELP

@Client.on_message(filters.channel & (filters.document | filters.video) & ~filters.forwarded, group=-1)
async def channel_receive_handler(bot: Client, broadcast: Message):
    if int(broadcast.chat.id) in BAN_CHNL:
        print("chat trying to get straming link is found in BAN_CHNL,so im not going to give stram link")
        return
    ban_chk = await db.is_banned(int(broadcast.chat.id))
    if (int(broadcast.chat.id) in BANNED_CHANNELS) or (ban_chk == True):
        await bot.leave_chat(broadcast.chat.id)
        return
    try:
        # फाइल का नाम निकालें
        file = broadcast.document or broadcast.video
        file_name = file.file_name if file else "Unknown File"

        # बॉट फाइल को BIN_CHANNEL में फॉरवर्ड करेगा
        msg = await broadcast.forward(chat_id=BIN_CHANNEL)

        # Stream & Download लिंक बनाए
        stream = f"{URL}watch/{msg.id}?hash={get_hash(msg)}"
        download = f"{URL}{msg.id}?hash={get_hash(msg)}"
        file_link = f"https://t.me/{BOT_USERNAME}?start=file_{msg.id}"
            
        await msg.reply_text(
            text=f"**Channel Name:** `{broadcast.chat.title}`\n**CHANNEL ID:** `{broadcast.chat.id}`\n**Rᴇǫᴜᴇsᴛ ᴜʀʟ:** {stream}",
            quote=True
            )
            
        # कैप्शन अपडेट करें
        new_caption = f"<i><a href='{CHANNEL}'>{file_name}</a></i>"

        # बटन बनाएं
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton(" Stream", url=stream),
             InlineKeyboardButton("Download", url=download)],
            [InlineKeyboardButton('Get File', url=file_link)]
        ])

        # चैनल मैसेज का कैप्शन और बटन अपडेट करें
        await bot.edit_message_caption(
            chat_id=broadcast.chat.id,
            message_id=broadcast.id,
            caption=new_caption,
            reply_markup=buttons,
            parse_mode=enums.ParseMode.HTML
        )

    except asyncio.exceptions.TimeoutError:
        print("Request Timed Out! Retrying...")
        await asyncio.sleep(5)  # 5 सेकंड वेट करके दोबारा कोशिश करें
        await channel_receive_handler(bot, broadcast)

    except FloodWait as w:
        print(f"Sleeping for {w.value}s due to FloodWait")
        await asyncio.sleep(w.value)

    except Exception as e:
        await bot.send_message(chat_id=BIN_CHANNEL, text=f"❌ **Error:** `{e}`", disable_web_page_preview=True)
        print(f"❌ Can't edit channel message! Error: {e}")

#dont Remove My Credit @MSLANDERS 
# For Any Kind Of Error Ask Us In Support Group @MSLANDERS_HELP
