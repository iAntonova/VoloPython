# # https://www.youtube.com/watch?v=p0A4CV4MWd0&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=12
# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
#                     datefmt='%m/%d/%Y %H:%M:%S')
# import helper # this will print the message from helper.py
# # 01/18/2024 20:00:19 - helper - INFO - Hello from helper
# # but if I don't want to print the message from helper.py (propagation), then I can do this: (40,41)
# # then nothing will be printed

# # --------------
# import logging
# import logging.config

# logging.config.fileConfig('logging.conf') # this will read the config file

# logger = logging.getLogger('simpleExample') # this will create a logger with the name of the module
# logger.debug('this is a debug message') # 2024-01-22 20:33:34,740 - simpleExample - DEBUG - this is a debug message

# --------------
# about capturing stack traces - could be helpful for debugging (trubleshooting)
# for expample if u run the code witch raises an exception, then u can capture the stack trace
# import logging

# try:
#     a = [1,2,3]
#     val = a[4]
# except IndexError as e:
#     logging.error(e, exc_info=True) # this will print the stack trace
#     # IndexError: list index out of range

# # or we don't know what exception will be raised
# import logging
# import traceback

# try:
#     a = [1,2,3]
#     val = a[4]
# except:
#     logging.error("the error is %s", traceback.format_exc()) # this will print the stack trace

# # --------------
# # let's talk about rotating files
# # when u have a lot of logs, then u can rotate them
# import logging
# from logging.handlers import RotatingFileHandler

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # roll over after 2KB, and keep backup logs app.log.1, app.log.2 , etc.
# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5) # this will create a handler that will print to the file
# logger.addHandler(handler)

# for _ in range(10000):
#     logger.info('Hello, world!') # this will print the message from helper.py

# # --------------
# # now let's talk about time rotating file handler
# import logging
# import time
# from logging.handlers import TimedRotatingFileHandler
# # and this will create a new file depending on how much time has passed
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # s, m, h, d, midnight, w0-w6
# handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5) # this will create a handler that will print to the file
# logger.addHandler(handler)

# for _ in range(6):
#     logger.info('Hello, world!')
#     time.sleep(5)

# --------------
# if u have a lot of modules and a lot of logged things, 
# especially if u use microservise architecture, then u can
# use JSON format for logging
# https://github.com/madzak/python-json-logger