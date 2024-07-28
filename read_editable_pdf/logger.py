import os
import logging

class CustomLogger:
    @staticmethod
    def get_logger(name: str, log_path:str):
        # Create a custom logger
        logger = logging.getLogger(name)

        # Set the level of the logger
        logger.setLevel(logging.DEBUG)

        # Define the log file path
        log_file_path = os.path.join(log_path, f'/Logs/{name}.log')

        # Check if the logger already has handlers to avoid duplicate logs
        if not logger.hasHandlers():
            # Create handlers
            console_handler = logging.StreamHandler()
            file_handler = logging.FileHandler(log_file_path)
            console_handler.setLevel(logging.DEBUG)
            file_handler.setLevel(logging.ERROR)

            # Create formatters and add them to the handlers
            console_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(console_format)
            file_handler.setFormatter(file_format)

            # Add handlers to the logger
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)

        return logger
#
# # Example usage
# if __name__ == "__main__":
#     logger = CustomLogger.get_logger(__name__)
#     logger.debug("This is a debug message")
#     logger.info("This is an info message")
#     logger.warning("This is a warning message")
#     logger.error("This is an error message")
#     logger.critical("This is a critical message")
