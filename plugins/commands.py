#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from buttons import Button 
from script import script  # pylint:disable=import-error

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    await bot.send_message(chat_id=update.chat.id, text=script.START_MSG.format(update.from_user.mention), parse_mode="html", disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(Button.START_BUTTONS), reply_to_message_id=update.message_id)

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(bot, update):
    await bot.send_message(chat_id=update.chat.id, text=script.HELP_MSG, parse_mode="html", disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(Button.HELP_BUTTONS), reply_to_message_id=update.message_id)
