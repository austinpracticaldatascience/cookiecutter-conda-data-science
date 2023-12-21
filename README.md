# Cookiecutter Kaggle Conda Data Science

_A logical, reasonably standardized, but flexible project structure for participating in Kaggle competitions, as a team._

## TL;DR

### If cloning from an existing team competition repo
1. Ensure you have either conda, mamba or micromamba installed
2. Ensure you have signed up for Kaggle & have your username and API key generated
3. Clone repo (not this one! The "child" repo)
4. Edit ```.env``` to your ```KAGGLE_USERNAME=``` and ```KAGGLE_KEY=```
5. Now follow the instructions in [install.md](https://github.com/austinpracticaldatascience/cookiecutter-conda-data-science/blob/main/%7B%7B%20cookiecutter.project_slug%20%7D%7D/install.md)
6. Run ```invoke getdata```

### If creating a new team competition project
1. Ensure your Kaggle credentials / username & API key are set
2. run:

	```bash
	pip install cookiecutter
	
	cookiecutter https://github.com/austinpracticaldatascience/cookiecutter-conda-data-science
	```

3. follow instructions on cookiecutter cli
4. run:

	```bash
	cd <project_slug>
		
	mamba env create -f environment_minimal.yml
		
	mamba activate <project_slug>
		
	pip install --editable .
		
	invoke getdata
    ```
5. *IMPORTANT*: Ensure you aren't exposing your API username & key in ```{{ cookiecutter.project_slug }}/.env```
6. run:  
    ```
	git push <your-new-github-project-repo>
	```
7. Share that repo with the group



## Requirements

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html): This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
pip install cookiecutter
```

or

``` bash
conda install -c conda-forge cookiecutter
```

## Create a new project

In a folder where you want your project generated:

```bash
cookiecutter https://github.com/austinpracticaldatascience/cookiecutter-conda-data-science
```

## Resulting directory structure

    ├── LICENSE
    ├── tasks.py           <- Invoke with commands like `notebook`.
    ├── README.md          <- The top-level README for developers using this project.
    ├── install.md         <- Detailed instructions to set up this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures         <- Generated graphics and figures to be used in reporting.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment.
    │
    ├── .here              <- File that will stop the search if none of the other criteria
    │                         apply when searching head of project.
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .)
    │                         so {{ cookiecutter.project_module_name }} can be imported.
    │
    └── {{ cookiecutter.project_module_name }}               <- Source code for use in this project.
        ├── __init__.py    <- Makes {{ cookiecutter.project_module_name }} a Python module.
        │
        ├── data           <- Scripts to download or generate data.
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling.
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions.
        │   ├── predict_model.py
        │   └── train_model.py
        │
        ├── utils          <- Scripts to help with common tasks.
            └── paths.py   <- Helper functions to relative file referencing across project.
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations.
            └── visualize.py

## Contributing guide

All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome.

## Credits

This cookiecutter was forked from [jvelezmagic](https://github.com/jvelezmagic/cookiecutter-conda-data-science)
