from pyrogram.types import *
from pyrogram.errors import *
from info import *
from pyrogram import Client, filters
from pyrogram import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 


async def forcesub(bot, update):
        try:
            await bot.get_chat_member(AUTH_CHANNEL, update.from_user.id)
        except UserNotParticipant:
            file_id = "CAACAgUAAxkBAAEFIihiuYjFehkzzJg6fBsp9NSddE2QSQACsAYAAseOyVXbaQF75owUgCkE"
            await bot.send_sticker(update.from_user.id, file_id)
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            return await bot.send_message(update.from_user.id,
            text=text,
            reply_markup=reply_markup,
            disable_web_page_preview=True) 

FORCESUB_TEXT = "WTF Join Our Chanel humm 😒.."

FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                InlineKeyboardButton('Join Group☄️', url='https://t.me/Emo_Bot_Support')
            ]])
print("Emo Fsub Working")
