#(©)Codeflix-Bots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href=https://t.me/rin_nanakura{7432102513}'>rin nanakura</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/ongoing_society'>ᴏɴɢᴏɪɴɢ sᴏᴄɪᴇᴛʏ</a>\n○ ᴀɴɪᴍᴇ sᴜʙ sᴏᴄɪᴇᴛʏ : <a href='https://t.me/anime_sub_society'>ᴀɴɪᴍᴇ sᴜʙ sᴏᴄɪᴇᴛʏ</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href='https://t.me/AHSS_HELP_ZONE'>sᴏᴄɪᴇᴛʏ ᴄʜᴀᴛ ᴢᴏɴᴇ</a>\n○ Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ : <a href='https://t.me/i_killed_my_clan'>๏ 𝐎ʙɪᴛᴏ ᴜᴄʜɪʜᴀ ๏</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('⛩️ ʜᴏᴍᴇ ⛩️ ', url='https://t.me/AHSS_HELP_ZONE')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
