import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

#Buttons & Msgs

DEVS_BTN = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Rishmika Sandanu', url='https://t.me/ImRishmika'),
                 InlineKeyboardButton('Wisula', url='https://t.me/wisula4')
                 ],
                 [
                 InlineKeyboardButton('π', callback_data="back_Clbs")
                 ]]
                  )

DEVS_MG = "π±We Are Emo Developers π"

helps_msg = """
βΈππππ πΈπ π΄πππ π°ππ πππππ π±πππ π·πππ πππππππ!
How to Use me 
Ex:- `Minecraft`
πYes It Simple Normally Send App No to bot 
**ππππ π²ππ π³π ππππ π±ππ?**
β‘ππππ π±ππ ππππ π±π πππππππ πΎπ πΎπ ππ πππ ππππππππ.
β‘ππππ π±ππ π·πππ 
      βͺπΌππ π°πππ
      βͺπΏππππππ π°πππ
      βͺπ»ππππ π°πππ
β‘ππππ π±ππ ππππ πΎπ½ πΈπππππ πΌπππ ππ ππππ πΈπππππ πΌπππ π°π ππππππ π°πππ
βπΌπππ πππππππ 
     β« @Emo_Bot_Support
βπππππππππ 
     β« @Emo_Bot_Support

     
                  `Emo π£πΎππΎππππΎππ π’ππππΊππΊπππππ±π°`
"""

HelpBack_Btn = InlineKeyboardMarkup([[
                InlineKeyboardButton('π', callback_data="HELP_BACK")
            ]])

ENSTART_BTN = InlineKeyboardMarkup([[
                InlineKeyboardButton('πHELPπ', callback_data="HELP_CLB")
            ],
            [
               InlineKeyboardButton('Apps Store Repo', url='https://github.com/EmoBot-Industry/Emo-Apps-Store-Bot')
               InlineKeyboardButton('π©βπ»Bot Devsπ©βπ»', callback_data="DevsCallback")
            ],
            [
                InlineKeyboardButton('</Emo Bot Industry<s/Κ>π±π°', url='https://t.me/Emo_Bot_Support')
            ],
            [
                InlineKeyboardButton('πSearch hereπ', switch_inline_query_current_chat=''),
                InlineKeyboardButton('βοΈGo inlineβοΈ', switch_inline_query='')
            ],
            [ 
                InlineKeyboardButton('π Switch Language', callback_data="SI_CHANGE")
            ]
        ])

ENSTART_MSG = "Hi Welcome to **Emo App Store Bot**π­ βClick Help To more Helpsβ‘"


CLOSE_BUTTON = InlineKeyboardMarkup([[
                InlineKeyboardButton('cloce', callback_data="cloce")
            ]])
