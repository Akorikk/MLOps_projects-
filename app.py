from src.mlopsproject.logger import logging
from src.mlopsproject.exception import CustomException
import sys
from src.mlopsproject.components.data_ingestion import DataIngestion
from src.mlopsproject.components.data_ingestion import DataIngestionConfig
from src.mlopsproject.components.data_transformation import DataTransformationConfig,DataTransformation


if __name__=="__main__":
    logging.info("The Execution has Started")


    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        

        data_transformation=DataTransformation()
        data_transformation.initiate_data_transormation(train_data_path,test_data_path) 


    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)