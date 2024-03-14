import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AFROTOMusic import LOGGER, app, userbot
from AFROTOMusic.core.call import Zelzaly
from AFROTOMusic.misc import sudo
from AFROTOMusic.plugins import ALL_MODULES
from AFROTOMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS
from AFROTOMusic.plugins.play.azan import azkar


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("كود جلسة الحساب المساعد غير مدعوم ...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AFROTOMusic.plugins" + all_module)
    LOGGER("ميــوزك الزعيم").info("تم تحميل الاضافات ...✓")
    await userbot.start()
    await Zelzaly.start()
    try:
        await Zelzaly.stream_call("https://telegra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("ميــوزك عفرتو").info(
            "خطأ .. قم بفتح المكالمة في مجموعة السجل الخاصه بك\n\nجارِ ايقاف بوت الميوزك . . ."
        )
        exit()
    except:
        pass
    await Zelzaly.decorators()
    LOGGER("ميــوزك الزعيم").info("MatrixThon")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ميــوزك الزعيم").info("جارِ ايقاف بوت الميوزك . . .")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
