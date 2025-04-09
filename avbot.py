from pyrogram.errors import UserNotParticipant, FloodWait
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Script import script
from info import AUTH_PICS, AUTH_CHANNEL, ENABLE_LIMIT, RATE_LIMIT_TIMEOUT, MAX_FILES, BAN_ALERT, ADMINS
import asyncio, time
from typing import (
    Union
)

rate_limit = {}


#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP


async def get_invite_link(bot, chat_id: Union[str, int]):
    try:
        invite_link = await bot.create_chat_invite_link(chat_id=chat_id)
        return invite_link
    except FloodWait as e:
        print(f"Sleep of {e.value}s caused by FloodWait ...")
        await asyncio.sleep(e.value)
        return await get_invite_link(bot, chat_id)
        
async def is_user_joined(bot, message: Message):
    if AUTH_CHANNEL and AUTH_CHANNEL.startswith("-100"):
        channel_chat_id = int(AUTH_CHANNEL)    # When id startswith with -100
    elif AUTH_CHANNEL and (not AUTH_CHANNEL.startswith("-100")):
        channel_chat_id = AUTH_CHANNEL     # When id not startswith -100
    else:
        return 200
    try:
        user = await bot.get_chat_member(chat_id=channel_chat_id, user_id=message.from_user.id)
        if user.status == "BANNED":
            await message.reply_text(
                text=BAN_ALERT.format(ADMINS),
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True
            )
            return False
    except UserNotParticipant:
        invite_link = await get_invite_link(bot, chat_id=channel_chat_id)
        if AUTH_PICS:
            ver = await message.reply_photo(
                photo=AUTH_PICS,
                caption=script.AUTH_TXT.format(message.from_user.mention),
                parse_mode=ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("❆ Jᴏɪɴ Oᴜʀ Cʜᴀɴɴᴇʟ ❆", url=invite_link.invite_link)
                ]]
                )
            )
        else:
            ver = await message.reply_text(
                text=script.AUTH_TXT.format(message.from_user.mention),
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("❆ Jᴏɪɴ Oᴜʀ Cʜᴀɴɴᴇʟ ❆", url=invite_link.invite_link)
                    ]]
                ),
                parse_mode=ParseMode.HTML
            )
        await asyncio.sleep(30)
        try:
            await ver.delete()
            await message.delete()
        except Exception:
            pass
        return False
    except Exception:
        await message.reply_text(
            text = f"<i>Sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ</i> <b><a href='https://t.me/AV_SUPPORT_GROUP'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></b>",
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True)
        return False
    return True

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP
    
async def is_user_allowed(user_id):
    """📌 यह फंक्शन चेक करेगा कि यूजर की फाइल लिमिट खत्म हुई है या नहीं"""
    current_time = time.time()

    if ENABLE_LIMIT:
        if user_id in rate_limit:
            file_count, last_time = rate_limit[user_id]
            if file_count >= MAX_FILES and (current_time - last_time) < RATE_LIMIT_TIMEOUT:
                remaining_time = int(RATE_LIMIT_TIMEOUT - (current_time - last_time))
                return False, remaining_time  # ❌ Limit Exceeded
            elif file_count >= MAX_FILES:
                rate_limit[user_id] = [1, current_time]  # ✅ Reset Limit
            else:
                rate_limit[user_id][0] += 1
        else:
            rate_limit[user_id] = [1, current_time]

    return True, 0  # ✅ Allowed

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP
    
