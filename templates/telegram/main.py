import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN
from command_handlers import start_router
from message_handlers import echo_router

dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(echo_router)


async def main() -> None:
    bot = Bot(
        token=BOT_TOKEN, # type: ignore
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())