from kaggle.api.kaggle_api_extended import KaggleApi
from kaggle.rest import ApiException
from dotenv import load_dotenv, find_dotenv
import zipfile
import pathlib
from {{ cookiecutter.project_module_name }}.utils.logging.loggers import data_logger

class KaggleData:
    def __init__(self):
        # load_dotenv(find_dotenv()) #TODO: determine if this is necessary
        self.competition_slug = "{{ cookiecutter.competition_slug }}"
        self.zippedfiles = None
        self.files = None

    def download(self):
        if not self.competition_slug:
            data_logger.error(f"competition_slug must be set in cookiecutter!")
            raise ValueError

        api = KaggleApi()
        try:
            api.authenticate()
        # TODO: add more specific exception handling
        except Exception as e:
            data_logger.error(f"Failed to authenticate with Kaggle API with error:\n{e}")
            raise ApiException
        
        try:
            data_logger.info(f"Downloading competition data from {self.competition_slug}")
            api.competition_download_files(self.competition_slug,
                                        path='data/raw',
                                        quiet=False)
            zippedfiles = list(pathlib.Path('data/raw').glob('*.zip'))
            if len(zippedfiles) > 0:
                data_logger.info(f"Downloaded {len(zippedfiles)} competition zip files")
                self.zippedfiles = zippedfiles
            else:
                data_logger.error("No zip files found in data/raw")
                raise FileNotFoundError
        except ApiException as e:
            data_logger.error(f"Failed to download data from {self.competition_slug} with error:\n{e}")
            raise ApiException

    def unzip(self):
        if self.zippedfiles is None:
            data_logger.error("No zip files found in data/raw")
            raise FileNotFoundError

        data_logger.info(f"Unzipping {len(self.zippedfiles)} zip files")
        unzippedfiles = []
        for zippedfile in self.zippedfiles:
            with zipfile.ZipFile(zippedfile, 'r') as zip_ref:
                zip_ref.extractall('data/raw')
                for file in zip_ref.namelist():
                    unzippedfiles.append(pathlib.Path('data/raw') / pathlib.Path(file))
        if len(unzippedfiles) > 0:
            data_logger.info(f"Extracted {len(unzippedfiles)} files from {len(self.zippedfiles)} zip files")
            self.files = unzippedfiles
        data_logger.info("Unzipping complete")