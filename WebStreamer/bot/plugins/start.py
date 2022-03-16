from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start', 'help']))
async def start(_, m: Message):
    await m.reply(f'Hi {m.from_user.mention(style="md")}, 
I'm A simple link Generator Bot !💯.

Send me any TELEGRAM file, I'll generate instant stream/download link for you!

Developed by @pravin_boopathi',
                
                  )


 



