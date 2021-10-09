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

from pyrogram.types import InlineKeyboardButton

class Button(object):

    START_BUTTONS = [[InlineKeyboardButton('🗣️ Feedback', url='https://t.me/zautebot'), InlineKeyboardButton('Channel 📢', url='https://t.me/TGBotsProJect'),],
                    [InlineKeyboardButton('🌀 Source', url='https://github.com/ZauteKm/Image-Editor-Bot'), InlineKeyboardButton('Dev 👨‍💻', url='https://t.me/ZauteKm'), InlineKeyboardButton('Bot Lists 🤖', url='https://t.me/BotzListBot'),],
                        [InlineKeyboardButton('🚨 Help & Informations 🚨', callback_data='help')]]

    HELP_BUTTONS = [[InlineKeyboardButton('🗣️ Feedback', url='https://t.me/zautebot'), InlineKeyboardButton('Channel 📢', url='https://t.me/TGBotsProJect'),],
                    [InlineKeyboardButton('🌀 Source', url='https://github.com/ZauteKm/Image-Editor-Bot'), InlineKeyboardButton('Dev 👨‍💻', url='https://t.me/ZauteKm'), InlineKeyboardButton('Bot Lists 🤖', url='https://t.me/BotzListBot'),],
                        [InlineKeyboardButton('🏠 Back to Home 🏠', callback_data='home')]]
