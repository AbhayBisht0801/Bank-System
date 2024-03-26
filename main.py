from src.Banking_System import logger
from src.Banking_System.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Banking_System.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME='Data Ingestion stage'

try:
    logger.info(f'>>>>stage{STAGE_NAME} started')
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>stage {STAGE_NAME} completed')
except Exception as e:
    logger.exception(e)
    raise e
STAGE_NAME='Base Model Trainer Stage'
try:
    logger.info(f'>>>>stage{STAGE_NAME} started')
    obj=PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>>stage {STAGE_NAME} completed')
except Exception as e:
    logger.exception(e)
    raise e