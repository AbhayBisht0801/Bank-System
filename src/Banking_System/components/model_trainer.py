import os
import urllib.request as request
import zipfile
import gdown
import pandas as pd
from src.Banking_System import logger
from src.Banking_System.utils.common import get_size
from src.Banking_System.config.configuration import TrainingConfig
import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from src.Banking_System.utils.common import evaluate_model_transaction,save_object,evaluate_model_creditscore
class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
      
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                shear_range=0.2,
                zoom_range=0.2,
                 horizontal_flip=True,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)



    
    def cnn_train(self):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )

  
    def transaction_model_train(self):
        Train_data=pd.read_csv(os.path.join(self.config.transaction_dir,'transaction_train.csv'))
        Test_data=pd.read_csv(os.path.join(self.config.transaction_dir,'transaction_test.csv'))

        try:
            X_train=Train_data.drop(columns=['isFraud','Unnamed: 0'])
            y_train=Train_data['isFraud']
            X_test=Test_data.drop(columns=['isFraud','Unnamed: 0'])
            y_test=Test_data['isFraud']
            models={
                'RandomForest':RandomForestClassifier(),
                'LogisticRegression':LogisticRegression(),
                'KNeighborsClassifier':KNeighborsClassifier(),
                'GradientBoostingClassifier':GradientBoostingClassifier(),
                'SVC':SVC(),
                'XGBClassifier':XGBClassifier()
            }
            model_report:dict=evaluate_model_transaction(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)
            best_model_score=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model=models[best_model_name]
            print(best_model_score,best_model)
            if best_model_score<0.9:
                raise Exception('No Best model found')
            logger.info(f'Best found model on both training and testing dataset for fraud')
            save_object(self.config.transaction_model,best_model)
            
        except Exception as e:
            raise e
    def creditscore_model_train(self):
        Train_data=pd.read_csv(os.path.join(self.config.credit_score_dir,'credit_train.csv'))
        Train_data.drop(columns=['Unnamed: 0'],inplace=True)
        Test_data=pd.read_csv(os.path.join(self.config.credit_score_dir,'credit_test.csv'))
        Test_data.drop(columns=['Unnamed: 0'],inplace=True)
        try:
            X_train=Train_data.drop(columns=['Credit Score'])
            y_train=Train_data['Credit Score']
            X_test=Test_data.drop(columns=['Credit Score'])
            y_test=Test_data['Credit Score']
            models={
                'RandomForest':RandomForestClassifier(),
                'LogisticRegression':LogisticRegression(),
                'KNeighborsClassifier':KNeighborsClassifier(),
                'GradientBoostingClassifier':GradientBoostingClassifier(),
                'SVC':SVC(),
                'XGBClassifier':XGBClassifier()
            }
            model_report:dict=evaluate_model_creditscore(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)
            best_model_score=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model=models[best_model_name]
            print(best_model_score,best_model)
            if best_model_score<0.9:
                raise Exception('No Best model found')
            logger.info(f'Best found model on both training and testing dataset for credit')
            save_object(self.config.credit_score_model,best_model)
            
        except Exception as e:
            raise e

            

            

                