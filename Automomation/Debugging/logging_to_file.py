import logging

# The configuration
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

# Logging the debugging details
debug_message = logging.debug('Some debugging details.')

# Logging the debugging information
debug_info = logging.info('The logging module is working.')

# Logging the debugging warning
debug_warning = logging.warning('An error message is about to be logged.')

# Logging the debugging warning
debug_error = logging.error('An error has occurred.')

# logging the debugging critical warning
debug_critical_message = logging.critical('The program is unable to recover!')
