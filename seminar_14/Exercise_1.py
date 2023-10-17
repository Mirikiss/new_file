import logging

logger = logging.getLogger(__name__)

logging.basicConfig(filename='mylog.log', filemode='w', encoding='UTF-8', level=logging.ERROR, 
                    style='{', format=format)

def func(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        logger.error(nsg=)
