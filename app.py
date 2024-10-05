from src.mlopsproject.logger import logging
from src.mlopsproject.exception import CustomException
import sys
from src.mlopsproject.components.data_ingestion import DataIngestion
from src.mlopsproject.components.data_ingestion import DataIngestionConfig

if __name__=="__main__":
    logging.info("The Execution has Started")


    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)