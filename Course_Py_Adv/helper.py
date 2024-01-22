import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
#                     datefmt='%m/%d/%Y %H:%M:%S') # this is the default 
#             # format https://docs.python.org/3/library/logging.html#logging.basicConfig

# # now we can have assecc to 5 levels of logging
# # DEBUG, INFO, WARNING, ERROR, CRITICAL
# logging.debug("This is a debug message")
# logging.info("This is a info message")
# logging.warning("This is a warning message")
# logging.error("This is a error message")
# logging.critical("This is a critical message")

# and if I run this:

# WARNING:root:This is a warning message
# ERROR:root:This is a error message
# CRITICAL:root:This is a critical message

# not all the messages are printed, because the default level is WARNING
# we can change it by setting basic config

# add this line to the beginning of the file
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S') 
# and after that:
# 01/18/2024 20:00:19 - root - DEBUG - This is a debug message
# 01/18/2024 20:00:19 - root - INFO - This is a info message
# 01/18/2024 20:00:19 - root - WARNING - This is a warning message
# 01/18/2024 20:00:19 - root - ERROR - This is a error message
# 01/18/2024 20:00:19 - root - CRITICAL - This is a critical message

# now if I want to log from different modules, then if's best practice not to use this rool logger
# and to create ur own logger
# comment all from above except the first line:
logger = logging.getLogger(__name__) # this will create a logger with the name of the module
logger.info("Hello from helper")
# and then in ur mail.py file: