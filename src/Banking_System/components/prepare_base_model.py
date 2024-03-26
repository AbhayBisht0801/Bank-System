import os
import urllib.request as request
import tensorflow as tf
from pathlib import Path
from src.Banking_System import logger
from src.Banking_System.utils.common import get_size
from src.Banking_System.config.configuration import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self,config:PrepareBaseModelConfig):
        self.config=config
    def get_base_model(self):
        self.model=tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )
        model=self.model
        self.save_model(path=self.config.base_model_path,model=self.model)
    @staticmethod
    def save_model(path:Path,model:tf.keras.Model):
        model.save(path)
    def prepare_full_model(self,model,classes,frozen_all,frozen_till,learning_rate,dropout_no):
        if frozen_all:
            for layer in model.layers:
                model.trainable=False
        elif (frozen_till is not None) and (frozen_till>0):
            for layer in model.layers[:frozen_till]:
                model.trainable=False
        flatten_in=tf.keras.layers.Flatten()(model.output)
        dense1=tf.keras.layers.Dense(units=256,activation='relu')(flatten_in)
        Normalization=tf.keras.layers.BatchNormalization()(dense1)
        dense2=tf.keras.layers.Dense(units=128,activation='relu')(Normalization)
        dropout=tf.keras.layers.Dropout(dropout_no)(dense2)
        dense3=tf.keras.layers.Dense(units=64,activation='relu')(dropout)
        dropout=tf.keras.layers.Dropout(dropout_no)(dense3)
        dense4=tf.keras.layers.Dense(units=32,activation='relu')(dropout)
        dropout=tf.keras.layers.Dropout(dropout_no)(dense4)
        dense5=tf.keras.layers.Dense(units=16,activation='relu')(dropout)
        prediction=tf.keras.layers.Dense(units=classes,activation='softmax')(dense5)
        full_model=tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction

        )
        full_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                          loss=tf.keras.losses.CategoricalCrossentropy(),
                          metrics=['accuracy'])
        return full_model
        
    def update_base_model(self):
        self.full_model=self.prepare_full_model(
                model=self.model,
                classes=self.config.params_classes,
                frozen_all=True,
                frozen_till=None,
                learning_rate=self.config.params_learning_rate,
                dropout_no=self.config.params_dropout
            )
        full_model=self.full_model
        full_model.summary()
        self.save_model(path=self.config.updated_base_model_path,model=self.full_model)


    @staticmethod
    def save_model(path:Path,model:tf.keras.Model):
        model.save(path)
        