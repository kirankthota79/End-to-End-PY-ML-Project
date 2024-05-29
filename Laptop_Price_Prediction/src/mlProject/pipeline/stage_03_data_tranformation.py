from mlProject.components.data_validation import DataValidation
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger
from mlProject.components.data_transformation import DataTransformation
from pathlib import Path

STAGE_NAME = "Data tranformation for model training"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
                
                if status == "True":
                    config = ConfigurationManager()
                    data_tranformation_config = config.get_data_ingestion_config()
                    data_tranformation = DataTransformation(config=data_tranformation_config)
                    x_train,x_test,y_train,y_test = data_tranformation.train_test_spliting()
                    return data_tranformation.transformation(x_train,x_test,y_train,y_test)
                
                else:
                    raise Exception("Your data not valid shcema or some error in pr processing")
        except Exception as e:
            print(e)
            
            
if __name__ =="__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj= DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
                    