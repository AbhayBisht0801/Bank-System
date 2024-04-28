from src.Banking_System.constants import *
from src.Banking_System.utils.common import read_yaml,create_directories
from src.Banking_System.entity.configentity import DataIngestionConfig
from src.Banking_System.entity.configentity import PrepareBaseModelConfig
from src.Banking_System.entity.configentity import TrainingConfig
class ConfigurationManager:
    def __init__(
            self,
            config_filepath=CONFIG_FILE_PATH,
            params_filepath=PARAMS_FILE_PATH
    ):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directories([config.root_dir])
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES,
            params_dropout=self.params.DROPOUT)
        return prepare_base_model_config

    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir,'data\\train')
        transaction_dir=self.config.data_ingestion.transaction_dir
        credit_score_dir=self.config.data_ingestion.credit_score_dir
        
        create_directories([
            Path(training.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            cnn_trained_model_path=Path(training.cnn_trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE,
            credit_score_model=Path(training.credit_score_model),
            transaction_model=Path(training.transaction_model),
            credit_score_dir=Path(credit_score_dir),
            transaction_dir=Path(transaction_dir)

        )

        return training_config