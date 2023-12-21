# log_config.py
import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger