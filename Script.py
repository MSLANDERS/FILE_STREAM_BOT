class script(object):
    START_TXT = """<b>Hᴇʏ {}, </b>\n\n<i>send me a file or add me as an admin to any channel to instantly generate file links.

Add me to your channel to instantly generate links for any downloadable media. Once received, I will automatically attach appropriate buttons to the post containing the URL.</i>\n\n<blockquote><a href=https://t.me/{}?startchannel&admin=post_messages+edit_messages+delete_messages>➜ 𝖠𝖽𝖽 𝖳𝗈 𝖢𝗁𝖺𝗇𝗇𝖾𝗅</a></blockquote>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.6 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    HELP_TXT = """<b>ʏᴏᴜ ᴅᴏɴ'ᴛ ɴᴇᴇᴅ ᴍᴀɴʏ ᴄᴏᴍᴍᴇɴᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ \n\nᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ғɪʟᴇs ᴀɴᴅ I ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴅɪʀᴇᴄᴛ ʙᴏᴡɴʟᴏᴀᴅ & sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋ\n\nᴀʟsᴏ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴀɴᴅ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀ 💥\n\nғᴏʀ ᴍᴏʀᴇ, ᴜꜱᴇ /help ᴄᴏᴍᴍᴀɴᴅ\nᴍᴏʀᴇ, ᴜꜱᴇ /about ᴄᴏᴍᴍᴀɴᴅ</b>"""

#Dont Remove My Credit @MSLANDERS 
# For Any Kind Of Error Ask Us In Support Group @MSLANDERS_HELP
    
    ADMIN_CMD_TXT = """<b>
    
ADMIN KI JAI HO 😎

/broadcast send massage users 
/users To get users details
/ban user/channel id dan
/unban user/channel id undan
/restart bot is restart</b>"""

    HELP2_TXT = """<b>Hᴏᴡ ᴛᴏ Uꜱᴇ Fɪʟᴇ ᴛᴏ Lɪɴᴋ Bᴏᴛ

Bᴀꜱɪᴄ Uꜱᴀɢᴇ:
• Sᴇɴᴅ ᴀɴʏ ғɪʟᴇ ᴏʀ ᴍᴇᴅɪᴀ ғʀᴏᴍ Tᴇʟᴇɢʀᴀᴍ
• Bᴏᴛ ᴡɪʟʟ ɢᴇɴᴇʀᴀᴛᴇ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴᴅ ꜱᴛʀᴇᴀᴍ ʟɪɴᴋꜱ
• Uꜱᴇ ᴛʜᴇꜱᴇ ʟɪɴᴋꜱ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴏʀ ꜱᴛʀᴇᴀᴍ ᴄᴏɴᴛᴇɴᴛ ᴛʜʀᴏᴜɢʜ ᴏᴜʀ ꜱᴇʀᴠᴇʀꜱ
• Fᴏʀ ꜱᴛʀᴇᴀᴍɪɴɢ, ᴘᴀꜱᴛᴇ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ʟɪɴᴋ ɪɴ ᴀɴʏ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ

Kᴇʏ Fᴇᴀᴛᴜʀᴇꜱ:
• Pᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛɪᴏɴ
• Dɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ꜱᴜᴘᴘᴏʀᴛ 
• Vɪᴅᴇᴏ ꜱᴛʀᴇᴀᴍɪɴɢ ᴄᴀᴘᴀʙɪʟɪᴛʏ
• Cʜᴀɴɴᴇʟ ꜱᴜᴘᴘᴏʀᴛ (Aᴅᴅ ʙᴏᴛ ᴀꜱ ᴀᴅᴍɪɴ)
• Cᴜꜱᴛᴏᴍ ꜱʜᴏʀᴛᴇɴᴇʀ ɪɴᴛᴇɢʀᴀᴛɪᴏɴ
• Uɴʟɪᴍɪᴛᴇᴅ ғɪʟᴇ ꜱɪᴢᴇ ꜱᴜᴘᴘᴏʀᴛ

Cʜᴀɴɴᴇʟ Uꜱᴀɢᴇ:
𝟷. Aᴅᴅ ʙᴏᴛ ᴀꜱ ᴀᴅᴍɪɴ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ
𝟸. Bᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴘʀᴏᴄᴇꜱꜱ ғɪʟᴇꜱ
𝟹. Lɪɴᴋꜱ ᴡɪʟʟ ʙᴇ ɢᴇɴᴇʀᴀᴛᴇᴅ ғᴏʀ ᴀʟʟ ᴍᴇᴅɪᴀ

⚠️ Iᴍᴘᴏʀᴛᴀɴᴛ Nᴏᴛᴇꜱ:
• Aʟʟ ʟɪɴᴋꜱ ᴀʀᴇ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴀɴᴅ ᴡᴏɴ'ᴛ ᴇxᴘɪʀᴇ
• Sʜᴀʀɪɴɢ ɪɴᴀᴘᴘʀᴏᴘʀɪᴀᴛᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪʟʟ ʀᴇꜱᴜʟᴛ ɪɴ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ
• Rᴇᴘᴏʀᴛ ᴀɴʏ ɪꜱꜱᴜᴇꜱ ᴛᴏ ᴏᴜʀ ꜱᴜᴘᴘᴏʀᴛ ᴛᴇᴀᴍ

🔞 ᴀᴅᴜʟᴛ ᴄᴏɴᴛᴇɴᴛ sᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ.

📮 Hᴇʟᴘ & Sᴜᴘᴘᴏʀᴛ:
• Uᴘᴅᴀᴛᴇꜱ: @MSLANDERS
• Sᴜᴘᴘᴏʀᴛ: @MSLANDERS_HELP

 <u><i>ʀᴇᴘᴏʀᴛ ʙᴜɢs ᴛᴏ  <a href='https://t.me/MSLANDERSTALK_BOT'>ᴅᴇᴠᴇʟᴏᴘᴇʀ</a></u></i></b>"""

#Dont Remove My Credit @MSLANDERS 
# For Any Kind Of Error Ask Us In Support Group @MSLANDERS_HELP
    
    LOG_TEXT = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""

    ABOUT_TXT = """<b>╔═══❰ {} ❱══════❍
║╭━━━━━━━━━━━━━━━━━━➣
║┣⪼🤖ᴍʏ ɴᴀᴍᴇ : {}
║┣⪼👦ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/MSLANDERSTALK_BOT'>ᴄʜᴀᴛ ᴏᴡɴᴇʀ</a>
║┣⪼❣️ᴜᴘᴅᴀᴛᴇ : <a href=https://t.me/mslanders>ʙᴀᴄᴋᴜᴘ ᴄʜᴀɴɴᴇʟ</a>
║┣⪼⏲️ʙᴏᴛ ᴜᴘᴛɪᴍᴇ :- {}
║┣⪼📡Hᴏsᴛᴇᴅ ᴏɴ : ᴋᴏʏᴇʙ 
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 
║┣⪼📚ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : v{} [ᴍᴏsᴛ sᴛᴀʙʟᴇ]
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍ </b>"""

#Dont Remove My Credit @MSLANDERS 
# For Any Kind Of Error Ask Us In Support Group @MSLANDERS_HELP
    
    AUTH_TXT = """<b>Dᴇᴀʀ {}!\n\nPʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ ! 😊\n\nDᴜᴇ ᴛᴏ sᴇʀᴠᴇʀ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ !</b>"""
    
    CAPTION_TXT = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>

<b>📧 ꜰɪʟᴇ ɴᴀᴍᴇ :- </b> <i><a href={}>{}</a></i>

<b>📦 ꜰɪʟᴇ sɪᴢᴇ :- </b> <i>{}</i>

<b><u><i>Tap To Copy Link 👇</u></i></b>

<b>🖥 Stream  : </b> <code>{}</code>

<b>📥 Download : </b> <code>{}</code>

<b>🚸 Nᴏᴛᴇ : LINK WON'T EXPIRE TILL I DELETE 👨‍💻</b>"""

#Dont Remove My Credit @MSLANDERS 
# For Any Kind Of Error Ask Us In Support Group @MSLANDERS_HELP
    
    CAPTION2_TXT = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>

<b>📧 ꜰɪʟᴇ ɴᴀᴍᴇ :- </b> <i><a href={}>{}</a></i>

<b>📦 ꜰɪʟᴇ sɪᴢᴇ :- </b> <i>{}</i>

<b><u><i>Tap To Copy Link 👇</u></i></b>

<b>📥 Download : </b> <code>{}</code>

<b>🚸 Nᴏᴛᴇ : LINK WON'T EXPIRE TILL I DELETE 👨‍💻</b>"""
    
#Dont Remove My Credit @MSLANDERS 
# For Any Kind Of Error Ask Us In Support Group @MSLANDERS_HELP
