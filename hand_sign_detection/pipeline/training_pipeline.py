import sys,os
from hand_sign_detection.logger import logging
from hand_sign_detection.exception import AppException
from hand_sign_detection.components.data_ingestion import DataIngestion
from hand_sign_detection.entity.artifacts_entity import DataIngestionArtifacts  
from hand_sign_detection.entity.config_entity import DataIngestionConfig
 


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        


    
    def start_data_ingestion(self)-> DataIngestionArtifacts:
        try: 
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from URL")

            data_ingestion = DataIngestion(
                data_ingestion_config =  self.data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact

        except Exception as e:
            raise AppException(e, sys)
        


    
 

        

    

    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
         

           

        
        except Exception as e:
            raise AppException(e, sys)