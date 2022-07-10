from asyncio import sleep
import platform
from resources.string import repotxt
from plugins.Buttons import homebtn
from pyrogram import Client as sree
from pyrogram import filters, __version__ as pyro
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


@sree.on_message(filters.command('help'))
async def help(sree, m: Message):
    nm = m.from_user.first_name
    uid = m.from_user.id
    chtid = m.chat.id
    await m.reply_sticker('CAACAgUAAx0CWOSA3AABBtl5YspfsV3UeUpFs3pfmeoy0UMM_tMAAn8FAAIvIkBW70JZlNo13zcpBA')
    await m.reply(f"""<b>Meow <code>{nm}</code> .</b>
<b><u>Commands</u></b>
/start : To Start the bot.
/help : To get Help Menu.
/ping or /on : To check Alive and ping of bot.
/repo or /source : To get Source Code of @{} .
/pgen : Use and explorer.
    ➥ <code>Work in PM only</code>
/sgen : Use and explorer.
    ➥ <code>Work in Group only</code>""",
        reply_markup=InlineKeyboardMarkup(homebtn),
        disable_web_page_preview=True,
    )

@sree.on_message(filters.command(['repo', 'source']))
async def sourcecd(sree, m: Message):
    nm = m.from_user.first_name
    uid = m.from_user.id
    chtid = m.chat.id
    await m.reply_sticker('CAACAgUAAx0CWOSA3AABBtl5YspfsV3UeUpFs3pfmeoy0UMM_tMAAn8FAAIvIkBW70JZlNo13zcpBA')
    await m.reply(
        repotxt.format(nm),
        reply_markup=InlineKeyboardMarkup(homebtn),
        disable_web_page_preview=True,
    )
