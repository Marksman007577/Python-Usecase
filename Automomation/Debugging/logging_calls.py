import logging

# The configuration
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# Logging the debugging details
debug_message = logging.debug('Some debugging details.')
print(debug_message)

# Logging the debugging information
debug_info = logging.info('The logging module is working.')
print(debug_info)

# Logging the debugging warning
debug_warning = logging.warning('An error message is about to be logged.')
print(debug_warning)

# Logging the debugging warning
debug_error = logging.error('An error has occurred.')
print(debug_error)

# logging the debugging critical warning
debug_critical_message = logging.critical('The program is unable to recover!')
print(debug_critical_message)