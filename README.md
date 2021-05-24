# Vegetation Restoration Monitoring
This is a repository for my Earth Analytics capstone project focused on the use of remote sensing and climate/weather data to monitor vegetation restoration at McKinley Mine in New Mexico. The goal of this project is to monitor the the trajectory of vegetation restoration measures using statistical modeling of a time series of remote sensing (Sentinel 2, Landsat 8) and weather/climate data. Through the case study of McKinley Mine the project will develop methods and workflows that focus specifically on restoration of arid rangeland environments. The developed workflows have potential to be applied to similar restoration contexts or be adapted to additional study sites.

## Description of the Repository 
* data: contains input data for the analysis workflow
* final_notebooks: sequentially numbered notebooks to duplicate the analysis
* working_notebooks: exploratory notebooks
* presentations

## Tools and Packages Used
* matplotlib
* numpy
* geopandas
* rasterio
* contextily
* folium
* sentinelhub

## Analysis Workflow
* Run the notebooks in final_notebooks in sequential order; specifics to follow...

## Example Usage
* working_notebooks/rs_time_series_seeding_units.ipynb: uses input shapefile for different seeding units to calculate NDVI time series, alter the start date to change the beginning of the Sentinel 2 time series
