# use credentials in .env file and kaggle api to download data
from {{ cookiecutter.project_module_name }}.utils.data.kaggle import KaggleData
from {{ cookiecutter.project_module_name }}.utils.data.preprocessing import DataProcessor
from dotenv import load_dotenv, find_dotenv

def main():
    """ Runs data processing scripts to:
     0. Download data from Kaggle API (data/raw)
     1. Unzip data (data/raw)
     2. Feature Engineering steps: TBD ... (data/processed)
     """
    kd = KaggleData()
    kd.download()
    kd.unzip()
    print("Data download complete. Available files:\n",
           *[f'{x.as_posix()}\n' for x in kd.files])

if __name__ == "__main__":
    load_dotenv(find_dotenv())
    main()