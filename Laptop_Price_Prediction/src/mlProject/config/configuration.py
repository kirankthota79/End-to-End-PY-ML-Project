from mlProject.constants import *
from mlProject.utils.common import read_yaml, crreate_directories
from mlProject.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTranformationConfig, ModelTrainerConfig, ModelEvaluationConfig
class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        crreate_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        crreate_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )
        
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        
        crreate_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir= config.unzip_data_dir,
            all_schema= schema,
            preprocessed_data=config.preprocessed_data
        )
        
        return data_validation_config
        
    def get_data_transformation_config(self) -> DataTranformationConfig:
        config = self.config.data_transformation
        
        crreate_directories([config.root_dir])
        
        data_transformation_config = DataIngestionConfig(
            root_dir= config.root_dir,
            data_path = config.data_path,
            transformer_path = config.transformer_path,
        )
        
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.KNeighborsRegressor
        schema = self.sechema.TARGET_COLUMN
        
        crreate_directories([config.root_dir])
        
        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            model_name= config.model_name,
            algorithm= params.algorithm,
            n_neighbors= params.n_neighbors,
            weights= params.weights,
            # target_column = schema.name
        )
        
        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.KNeighborsRegressor
        schema = self.schema.TARGET_COLUMN
        
        crreate_directories([config.root_dir])
        
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            transformer_path= config.transformer_path,
            model_path= config.model_path,
            all_params= params,
            metric_file_name= config.metric_file_name,
            target_column= schema.name,
            mlflow_uri="https://dagshub.com/kharramahendra/Laptop-Price---End-to-End-ML-Project.mlflow",
        )
        
        return model_evaluation_config