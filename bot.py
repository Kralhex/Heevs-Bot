import logging

from secret import BOT_TOKEN
import command_handler

# Logger and Handler Configuration
logger = logging.getLogger('nextcord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='nextcord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Run Bot
command_handler.bot.run(token = BOT_TOKEN, log_handler=None)	