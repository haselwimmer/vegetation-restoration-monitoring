# Vegetation Restoration Monitoring
This is a repository for my Earth Analytics capstone project focused on the use of remote sensing and climate/weather data to monitor vegetation restoration at McKinley Mine in New Mexico. The goal of this project is to monitor the the trajectory of vegetation restoration measures using statistical modeling of a time series of remote sensing (Sentinel 2, Landsat 8) and weather/climate data. Through the case study of McKinley Mine the project will develop methods and workflows that focus specifically on restoration of arid rangeland environments. The developed workflows have potential to be applied to similar restoration contexts or be adapted to additional study sites.

## Description of the Repository 
* data: contains input data for the analysis workflow
* final_notebooks: sequentially numbered notebooks to duplicate the analysis
* working_notebooks: exploratory notebooks
* presentations
* vegrestoretools: contains module with custom functions

## Tools and Packages Used
* matplotlib
* numpy
* geopandas
* rasterio
* contextily
* folium
* sentinelhub

## Setup

To set up this repository, you will need to:

1. Create the conda environment included in the repository, and
2. run the `main` bash script.

### Conda Environment Setup

To setup the project environment, first,  make sure that anaconda or
Miniconda are installed on your machine. We prefer miniconda for this Environment
but either should work. Then,

1. In bash, `cd` to the `vegetation-restoration-monitoring` repo
2. Install the environment file

```
$ cd vegetation-restoration-monitoring
$ conda env create -f environment.yml
```

#### OPTIONAL - Package Setup

Activate your workflow environment:

```bash
$ conda activate earth-analytics-python
```

Install the included Python package.

```bash
$ pip install -e .

```

### Run the Bash Script To Create the Final Blog Post

The bash script runs the 'final_blog' notebook in the 'final_notebooks' directory. To run the bash script, you have to ensure you are in the `final_notebooks`
directory within `vegetation-restoration-monitoring`.

First, activate the workflow environment:

```
$ conda activate earth-analytics-python
```

Then, make sure you are in the 'final_blog' directory. Run the main workflow:

```
$ cd vegetation-restoration-monitoring
```
##  Run Workflow Using Bash Directly

Now you should be able to run the bash script without any errors.

```
$ . main.sh
```

The final output, `final_blog.html`, will be in the `final_notebooks` directory.
