from infrastructure.logger import get_logger


logger=get_logger(
    "ERROR"
)



def handle_error(
        component,
        error
):


    logger.error(
        f"{component}: {type(error).__name__} {error}"
    )


    return {


        "component":component,

        "error":str(error),

        "recovered":False

    }