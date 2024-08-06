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
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>𝗞𝗹𝗲𝗶𝗻 𝗠𝗼𝗿𝗲𝘁𝘁𝗶 𝚃 𝚑 𝚎 𝙵 𝚘 𝚘 𝚕</a>\n○ main channel: <a href='@Ani3lix_clan'>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ close", callback_data = "close"),
                    InlineKeyboardButton('🍁 support', url='https://t.me/Anim3chat')
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
