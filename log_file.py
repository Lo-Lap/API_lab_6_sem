import sys
import logging
from logging import StreamHandler, Formatter, FileHandler

# logging.basicConfig(level=logging.INFO,
#                     format='[%(asctime)s: %(levelname)s] - %(message)s')

logger = logging.getLogger("logger_bot")

logger.setLevel(logging.INFO)

handler = StreamHandler(stream=sys.stdout)
handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
file_handler = FileHandler(filename='log/logger_bot.log')
file_handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))

logger.addHandler(handler)
logger.addHandler(file_handler)


handler_http = StreamHandler(stream=sys.stdout)
handler_http.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
file_handler_http = FileHandler(filename='log/logger_http.log')
file_handler_http.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))

logger_http = logging.getLogger("logger_http")
logger_http.setLevel(logging.INFO)

logger_http.addHandler(handler_http)
logger_http.addHandler(file_handler_http)
