from DeepClassifier.components import PrepareCallback
from DeepClassifier.config import ConfigurationManager
from DeepClassifier import logger

STAGE_NAME = "Prepare Callbacks"


def main():
    config = ConfigurationManager()
    prepare_callbacks_config = config.prepare_callbacks_config()
    prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
    prepare_callbacks.get_tb_ckpt_callbacks()


if __name__ == "__main__":
    try:
        logger.info(f"********************************")
        logger.info(
            f"<<<< Stage {STAGE_NAME} started <<<<<\n\n"
        )

        main()
        logger.info(
            f"<<<< Stage {STAGE_NAME} completed successfully <<<<<\n\nx============x"
        )
    except Exception as e:
        logger.exception(e)
        raise e
