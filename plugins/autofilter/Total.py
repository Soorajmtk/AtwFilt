import logging
import shutil
import psutil
from pyrogram import Client as illuzX, filters as Worker
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from utils import get_size
from plugins.database.autofilter_db import Media
from plugins.database.users_chats_db import db
from config import ADMINS
logger = logging.getLogger(__name__)


@illuzX.on_message(Worker.command("mydb") & Worker.user(ADMINS) & ~Worker.edited)
async def status(bot,  Message):
        total = await Media.count_documents()
        users = await db.total_users_count()
        chats = await db.total_chat_count()
        monsize = await db.get_db_size()
        free = 536870912 - monsize
        monsize = get_size(monsize)
        free = get_size(free)
        await Message.edit_text(
            text=AtwFilt.STATUS_TXT.format(total, users, chats, monsize, free),
            reply_markup=reply_markup,
            parse_mode='html'
        )