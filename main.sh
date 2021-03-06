#!/bin/bash

jupyter nbconvert --to notebook --execute notebooks/1-process-seeding-unit-vectors.ipynb
jupyter nbconvert --to notebook --execute notebooks/2-landsat-time-series.ipynb
jupyter nbconvert --to notebook --execute notebooks/3-preprocess-rs-timeseries.ipynb
jupyter nbconvert --to notebook --execute notebooks/4-meteorology-timeseries.ipynb
jupyter nbconvert --to notebook --execute notebooks/5-data-integration-analysis.ipynb
jupyter nbconvert --to notebook --execute notebooks/6-plotting.ipynb
jupyter nbconvert --to html_embed --no-input --output-dir='notebooks' --execute notebooks/7-final_blog.ipynb