from DeepClassifier.components import PrepareBaseModel
from DeepClassifier.config import ConfigurationManager
from DeepClassifier import logger

STAGE_NAME = "Prepare Base Model"


def main():
    config = ConfigurationManager()
    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
    prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info("********************************")
        logger.info(f"<<<< Stage {STAGE_NAME} started <<<<<\n\nx============x")

        main()
        logger.info(
            f"<<<< Stage {STAGE_NAME} completed successfully <<<<<\n\nx============x"
        )
    except Exception as e:
        logger.exception(e)
        raise e
