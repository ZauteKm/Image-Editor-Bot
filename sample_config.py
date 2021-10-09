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

import os


class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    # The Telegram API things from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")

    # Get this api from https://www.remove.bg/b/background-removal-api
    RemoveBG_API = os.environ.get("RemoveBG_API", "")

    # Get this api from https://www.remove.bg/b/background-removal-api
    REMOVEBG_API = os.environ.get("REMOVEBG_API", "")

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # Update channel for Force Subscribe
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")

    # dict to hold the ReQuest queue
    ADL_BOT_RQ = {}

    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = int(os.environ.get("TIME_LIMIT", ""))
