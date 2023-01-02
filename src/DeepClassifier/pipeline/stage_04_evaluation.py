from DeepClassifier.components import Evaluation
from DeepClassifier.config import ConfigurationManager
from DeepClassifier import logger

STAGE_NAME = "Evaluation"


def main():
    config = ConfigurationManager()
    val_config = config.get_validation_config()
    evaluation = Evaluation(val_config)
    evaluation.evaluation()
    evaluation.save_score()


if __name__ == "__main__":
    try:
        logger.info("********************************")
        logger.info(f"<<<< Stage {STAGE_NAME} started <<<<<\n\n")

        main()
        logger.info(
            f"<<<< Stage {STAGE_NAME} completed successfully <<<<<\n\nx============x"
        )
    except Exception as e:
        logger.exception(e)
        raise e
