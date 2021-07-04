[![DOI](https://zenodo.org/badge/366880764.svg)](https://zenodo.org/badge/latestdoi/366880764)

# Vegetation Restoration Monitoring
This is a repository for my Earth Analytics capstone project focused on the use of remote sensing and climate/weather data to monitor vegetation restoration at McKinley Mine in New Mexico. The goal of this project is to monitor the the trajectory of vegetation restoration measures using a time series of NDVI from Landsat 8 and by comparing this with meteorological data. Through the case study of McKinley Mine the project will develop methods and workflows that focus specifically on restoration of arid rangeland environments. The developed workflows have potential to be applied to similar restoration contexts or be adapted to additional study sites.

## Description of the Repository 
* notebooks: sequentially numbered notebooks to duplicate the analysis
* vegrestoretools: contains module with custom functions
* environment.yml: environment file
* LICENSE: license file
* main.sh: bash file to run the workflow
* README.md: this file
* setup.py: setup file for the vegrestoretools module

## Tools and Packages Used
* matplotlib
* numpy
* geopandas
* rasterio
* rasterstats
* contextily
* folium
* sentinelhub
* ee
* plotly

## Setup

To set up this repository, you will need to:

1. Create the conda environment included in the repository, and
2. install the included python package (vegrestoretools)

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

### Package Setup

Activate your workflow environment:

```bash
$ conda activate veg-restore
```

Install the included Python package.

```bash
$ pip install -e .

```

## Configuration
* The workflow is initialized using a shapefile containing polygons for seeding units at McKinley Mine; these data cannot be freely shared. The workflow can be adapted to other sites using seeding unit data, key data fields are: 1) Year of seeding, and 2) type of seeding (e.g. seeding, re-seeding, interseeding). Please contact me and I can provide a template for the seeding unit shapefile that I have worked with. 
* The workflow requires the definition of a working directory that is used: 1) as the location for the seeding unit shapefile; 2) to store downloaded Landsat 8 data.
* The workflow uses the SentinelHub API (www.sentinel-hub.com) and requires a SentinelHub account and you to define a configuration instance (https://www.sentinel-hub.com/develop/dashboard/) for Landsat 8. The workflow requires you to enter an "instance_id", "sh_client_id", and "sh_client_secret" to enable the use of the SentinelHub configuration; these should be entered into `notebooks/landsat_setup.ini`
* The workflow uses Google Earth Engine to access the gridMET metorological data; you will require a GEE account and to perform a one-time authorization by uncommenting the code in `notebooks/4-meteorology-timeseries`

## Running the workflow
The workflow can be run either by running the notebooks sequentially or using the bash script.

### Run the notebooks sequentially
1. Import and processing the seeding unit vectors with: notebooks/1-process-seeding-unit-vectors.ipynb
2. Download Landsat 8 NDVI data and create time series with: notebooks/2-landsat-time-series.ipynb
3. Clean and smooth the time series data with: notebooks/3-preprocess-rs-timeseries.ipynb
4. Download meteorological data with: notebooks/4-meteorology-timeseries.ipynb
5. Integrate and clean the NDVI and meteorological time series data with: notebooks/5-data-integration-analysis.ipynb
6. Create the final blog post with: notebooks/6-final_blog.ipynb

### Run the Bash Script To Create the Final Blog Post

The bash script runs the '6-final_blog' notebook in the 'notebooks' directory. To run the bash script, you have to ensure you are in the `notebooks` directory within `vegetation-restoration-monitoring`.

First, activate the workflow environment:

```
$ conda activate veg-restore
```

Then, make sure you are in the 'notebooks' directory. Run the main workflow:

```
$ cd notebooks
```

Now you should be able to run the bash script without any errors.

```
$ . main.sh
```

The final output, `6-final_blog.html`, will be in the `notebooks` directory.
