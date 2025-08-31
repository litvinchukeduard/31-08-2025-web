import logging

# logger = logging.getLogger(__name__)
# logging.basicConfig(filename='app.log', level=logging.DEBUG)

# number_one = 1
# logger.info(f"number_one is set to {number_one}")
# number_two = 0
# logger.info(f"number_two is set to {number_two}")

# logger.debug(f"Trying to divide {number_one} by {number_two}")
# try:
#     result = number_one / number_two
#     print(result)
# except Exception as e:
#     print("Please try again...")
#     logger.exception("Something happened to the division logic")
#     logger.exception(e)


class Logger:
    instance = None

    def __new__(cls):
        # print("Calling new")
        if Logger.instance is None:
            Logger.instance = super(Logger, cls).__new__(cls)
        return Logger.instance

    def __init__(self):
        # print("Calling init")
        logger = logging.getLogger(__name__)
        logging.basicConfig(filename='app.log', level=logging.DEBUG)
        self.log = logger

if __name__ == '__main__':
    logger_one = Logger()
    logger_two = Logger()

    print(logger_one == logger_two)
