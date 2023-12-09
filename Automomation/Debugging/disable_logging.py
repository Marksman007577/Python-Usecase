"""Since logging.disable() will disable all messages after it, you will probably
want to add it near the import logging line of code in your program. This
way, you can easily find it to comment out or uncomment that call to enable
or disable logging messages as needed."""
import logging
logging.disable(logging.CRITICAL)  # it is placed here because, it clears the logging after it
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')
