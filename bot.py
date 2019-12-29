from telegram.ext import Updater, CommandHandler, MessageHandler, Filters # Updater - для запуска бота, CommandHandler - для обработки команд, MessageHendler - обработчик сообщений, Filtres - выбор типа сообщений (текст,картинка и т.п)
import logging # импорт функции логирования событий
import settigns # импорт апи с другого файла

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', 
                    level=logging.INFO, 
                    filename='bot.log') # сохранение логов asctime - время ошибки level name - уровень важности события message - что произошло в событии

# Функция, соединяющая с платформой телеграм, тело бота

def main():
    mybot = Updater(settigns.API_KEY, use_context=True) # соединение бота с телеграмом по API ключу

    logging.info('Запуск бота...') # сообщеиние в файл логов о запуске бота

    dp = mybot.dispatcher # переменная для сокращения кода
    dp.add_handler(CommandHandler('start', start_message)) # передает команду для входящих сообщений, 1 - сама команда /start, 2 - функция
    dp.add_handler(MessageHandler(Filters.text, send_message)) # Реакция на текстовое сообщение

    mybot.start_polling() # запуск бота
    mybot.idle() # заставляет бота работать бесконечно
 
def start_message(update, context): # функция отвечающая за команду /start, аргументы обязательны
    text = 'Нажата кнопка /start'
    logging.info(text) # логирование команды start
    update.message.reply_text(text) # простой ответ пользователю

def send_message(update, context):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text) # кладем в переменную сообщение пользователя
    update.message.reply_text(user_text) # эхо сообщение

# Вызов самой функции которая запускает бота

main()