from src.Banking_System.config.configuration import ConfigurationManager
from src.Banking_System import logger
from src.Banking_System.components.model_trainer import Training

STAGE_NAME='Prepare base Model'

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        model_training_config=config.get_training_config()
        training=Training(config=model_training_config)
        training.cnn_train()
        training.transaction_model_train()
        training.creditscore_model_train()

if __name__=='__main__':
    try:
        logger.info(f'>>>>>stage{STAGE_NAME} has Started')
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>stage{STAGE_NAME} has Completed')
    except Exception as e:
        logger.exception(e)
        raise e


        