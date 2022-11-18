from src.telegramItegraBot import TelegramBot
from src.driveItegraBot import driveBot
# bot = TelegramBot()
# bot.start()

driveBot = driveBot()
print(driveBot.get_data())
