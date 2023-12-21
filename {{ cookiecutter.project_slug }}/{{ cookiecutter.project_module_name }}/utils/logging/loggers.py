# loggers.py
import logging
from {{ cookiecutter.project_module_name }}.utils.logging.log_config import setup_logger


# Create a logger for data related tasks
data_logger = setup_logger('data_logger', 'data.log', level=logging.INFO)

# Create a logger for model related tasks
model_logger = setup_logger('model_logger', 'model.log', level=logging.INFO)

# Create a logger for Kaggle API interactions
kaggle_api_logger = setup_logger('kaggle_api_logger', 'kaggle_api.log', level=logging.INFO)