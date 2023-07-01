from aiogram import Bot, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN_API = '6310614308:AAEYQ00hVrMes8PGiAs4u3t2YI6tZKtEAkk'

storage = MemoryStorage()
bot = Bot(TOKEN_API, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)