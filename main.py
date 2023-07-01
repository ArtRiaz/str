from aiogram import types, executor
from create_bot import dp, bot


async def on_startup(_):
    print('Бот запущен')

@dp.message_handler()
async def start(message: types.Message):
    await message.answer('Привет')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)
