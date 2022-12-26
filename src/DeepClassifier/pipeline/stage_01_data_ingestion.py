from DeepClassifier.components import DataIngestion
from DeepClassifier.config import ConfigurationManager
from DeepClassifier import logger

STAGE_NAME = "Data Ingestion Stage"

def main():
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()




if __name__ == '__main__':
    try:
        logger.info(f"\n\n>>>> Stage {STAGE_NAME} started >>>>>")
        main()
        logger.info(f"<<<< Stage {STAGE_NAME} completed successfully <<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e
