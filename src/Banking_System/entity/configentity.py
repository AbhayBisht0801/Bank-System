
from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir:Path
    base_model_path:Path
    updated_base_model_path:Path
    params_image_size:list
    params_learning_rate:float
    params_include_top:bool
    params_weights:str
    params_classes:int
    params_dropout:float

from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class TrainingConfig:
    root_dir:Path
    cnn_trained_model_path:Path
    updated_base_model_path:Path
    training_data:Path
    params_epochs:int
    params_batch_size:int
    params_image_size:list
    credit_score_model:Path
    transaction_model:Path
    params_is_augmentation: bool
    transaction_dir:Path
    credit_score_dir:Path
    


