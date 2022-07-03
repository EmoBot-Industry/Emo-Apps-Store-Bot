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
                 InlineKeyboardButton('🔙', callback_data="back_Clbs")
                 ]]
                  )

DEVS_MG = "🌱We Are Emo Developers 🌟"

helps_msg = """
⸙𝚃𝚑𝚒𝚜 𝙸𝚜 𝙴𝚙𝚒𝚌 𝙰𝚙𝚙 𝚂𝚝𝚘𝚛𝚎 𝙱𝚘𝚝𝚜 𝙷𝚎𝚕𝚙 𝚂𝚎𝚌𝚝𝚒𝚘𝚗!
How to Use me 
Ex:- `Minecraft`
😂Yes It Simple Normally Send App No to bot 
**𝚆𝚑𝚊𝚝 𝙲𝚊𝚗 𝙳𝚘 𝚃𝚑𝚒𝚜 𝙱𝚘𝚝?**
➡𝚃𝚑𝚒𝚜 𝙱𝚘𝚝 𝚆𝚒𝚕𝚕 𝙱𝚎 𝚁𝚞𝚗𝚗𝚒𝚗𝚐 𝙾𝚗 𝙾𝚠𝚎𝚛 𝚊𝚙𝚔 𝚍𝚊𝚝𝚊𝚋𝚊𝚜𝚎.
➡𝚃𝚑𝚒𝚜 𝙱𝚘𝚝 𝙷𝚊𝚟𝚎 
      ▪𝙼𝚘𝚍 𝙰𝚙𝚔𝚜
      ▪𝙿𝚛𝚎𝚖𝚒𝚞𝚖 𝙰𝚙𝚔𝚜
      ▪𝙻𝚊𝚛𝚐𝚎 𝙰𝚙𝚔𝚜
➡𝚃𝚑𝚒𝚎 𝙱𝚘𝚝 𝚆𝚘𝚛𝚔 𝙾𝙽 𝙸𝚗𝚕𝚒𝚗𝚎 𝙼𝚘𝚘𝚍 𝚂𝚠𝚑𝚒𝚝𝚑 𝙸𝚗𝚕𝚒𝚗𝚎 𝙼𝚘𝚘𝚍 𝙰𝚗 𝚂𝚎𝚊𝚛𝚌𝚑 𝙰𝚙𝚔𝚜
✔𝙼𝚘𝚛𝚎 𝚄𝚙𝚍𝚊𝚝𝚎𝚜 
     ▫ @Emo_Bot_Support
✔𝚀𝚞𝚎𝚜𝚝𝚒𝚘𝚗𝚜 
     ▫ @Emo_Bot_Support

     
                  `Emo 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋𝗌 𝖢𝗈𝗆𝗉𝖺𝗋𝖺𝗍𝗂𝗈𝗇🇱🇰`
"""

HelpBack_Btn = InlineKeyboardMarkup([[
                InlineKeyboardButton('🔙', callback_data="HELP_BACK")
            ]])

ENSTART_BTN = InlineKeyboardMarkup([[
                InlineKeyboardButton('🆘HELP🆘', callback_data="HELP_CLB")
            ],
            [
               InlineKeyboardButton('Apps Store Repo', url='https://github.com/EmoBot-Industry/Emo-Apps-Store-Bot')
               InlineKeyboardButton('👩‍💻Bot Devs👩‍💻', callback_data="DevsCallback")
            ],
            [
                InlineKeyboardButton('</Emo Bot Industry<s/ʟ>🇱🇰', url='https://t.me/Emo_Bot_Support')
            ],
            [
                InlineKeyboardButton('🔍Search here🔄', switch_inline_query_current_chat=''),
                InlineKeyboardButton('↗️Go inline↗️', switch_inline_query='')
            ],
            [ 
                InlineKeyboardButton('🔄 Switch Language', callback_data="SI_CHANGE")
            ]
        ])

ENSTART_MSG = "Hi Welcome to **Emo App Store Bot**🎭 ✓Click Help To more Helps⚡"


CLOSE_BUTTON = InlineKeyboardMarkup([[
                InlineKeyboardButton('cloce', callback_data="cloce")
            ]])
