import logging


def get_logger(name):

    logger=logging.getLogger(name)


    if not logger.handlers:


        handler=logging.FileHandler(
            "trading_ai.log"
        )


        formatter=logging.Formatter(

            "%(asctime)s | %(levelname)s | %(message)s"

        )


        handler.setFormatter(
            formatter
        )


        logger.addHandler(
            handler
        )


        logger.setLevel(
            logging.INFO
        )


    return logger