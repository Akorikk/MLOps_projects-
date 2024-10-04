from src.mlopsproject.logger import logging
from src.mlopsproject.exception import CustomException
import sys

if __name__=="__main__":
    logging.info("The Execution has Started")


    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)