# Logger is a tool used to record messages from your program while it runs, which can help you debug, monitor
# and maintain your code more effectively. it's part of the built-in logging module in python

import logging

#configure logging
logging.basicConfig(
    level = logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',   # You can remove this line to log to console
    filemode ='a'
)

def divide(a,b):
    logging.info(f'Dividing {a} by {b}')
    try:
        result = a / b
        logging.debug(f'Result : {result}')
        return result
    except ZeroDivisionError:
        logging.error("Error : Tried to divide by zero!")
        return None

#Test

divide(10,2)
divide(10,0)
