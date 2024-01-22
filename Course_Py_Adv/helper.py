# import logging
# # logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
# #                     datefmt='%m/%d/%Y %H:%M:%S') # this is the default 
# #             # format https://docs.python.org/3/library/logging.html#logging.basicConfig

# # # now we can have assecc to 5 levels of logging
# # # DEBUG, INFO, WARNING, ERROR, CRITICAL
# # logging.debug("This is a debug message")
# # logging.info("This is a info message")
# # logging.warning("This is a warning message")
# # logging.error("This is a error message")
# # logging.critical("This is a critical message")

# # and if I run this:

# # WARNING:root:This is a warning message
# # ERROR:root:This is a error message
# # CRITICAL:root:This is a critical message

# # not all the messages are printed, because the default level is WARNING
# # we can change it by setting basic config

# # add this line to the beginning of the file
# # logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S') 
# # and after that:
# # 01/18/2024 20:00:19 - root - DEBUG - This is a debug message
# # 01/18/2024 20:00:19 - root - INFO - This is a info message
# # 01/18/2024 20:00:19 - root - WARNING - This is a warning message
# # 01/18/2024 20:00:19 - root - ERROR - This is a error message
# # 01/18/2024 20:00:19 - root - CRITICAL - This is a critical message

# # now if I want to log from different modules, then if's best practice not to use this rool logger
# # and to create ur own logger
# # comment all from above except the first line:
# logger = logging.getLogger(__name__) # this will create a logger with the name of the module
#     # __name__ - global variable that will be replaced with the name of the module
# # logger.info("Hello from helper")
# # and then in ur mail.py file
# # --------------
# logger.propagate = False # this will prevent the message to be printed twice
# logger.info("Hello from helper") # this will print the message from helper.py

# --------------
# How to show different log handlers:
import logging

logger = logging.getLogger(__name__) # __name__ - this will create a logger with the name of the module

# create my handler
stream_h = logging.StreamHandler() # this will create a handler that will print to the console
file_h = logging.FileHandler('file.log') # this will create a handler that will print to the file

# then for each handler u want to set level and the format
stream_h.setLevel(logging.WARNING) # this will set the level of the handler
file_h.setLevel(logging.ERROR) # this will set the level of the handler

# now we also specify some formater, so we say
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s') # this will set the format of the handler
stream_h.setFormatter(formatter) 
file_h.setFormatter(formatter) 

# this will add the handler to the logger
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("This is a warning")
logger.error("This is a error") # this will be printed to the file
# __main__ - WARNING - This is a warning
# __main__ - ERROR - This is a error

