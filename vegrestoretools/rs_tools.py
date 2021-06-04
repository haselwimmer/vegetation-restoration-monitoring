def FisToDataframe(fis_data):
    
    """ Creates a DataFrame from list of FIS responses
    
    Parameters
    -----------
    fis_data : list
        list of data responses from FIS request

    Returns
    -----------
    output : pandas dataframe
        DF containing formatted results
    
    """
    
    # Import functions
    import pandas as pd
    from sentinelhub.time_utils import parse_time
    
    # Setup columns in df
    columns = ['date', 'min', 'max', 'mean', 'stDev'] # Columns for band ratio result
    clm_columns = ['clm_mean'] # Columns for Cloud Mask
    snw_columns = ['snw_mean'] # Columns for snow detection
    
    # Lists to store results
    data = []
    clm_data = []
    snw_data = []
    
    
    # Loops over multipolygons?
    for fis_response in fis_data:
            
            i = 0
            # Loop over channels
            for channel, channel_stats in fis_response.items():
                
                # Results channel
                if channel == 'C0':
                    for stat in channel_stats:
                        row = [parse_time(stat['date'])]
                        for column in columns[1:]:
                            row.append(stat['basicStats'][column])
                        data.append(row)
                
                # CLM channel
                elif channel == 'C1':
                    for stat in channel_stats:
                        row = [stat['basicStats']['mean']]
                        clm_data.append(row)
                
                # SNW channel
                else: 
                    for stat in channel_stats:
                        row = [stat['basicStats']['mean']]
                        snw_data.append(row)                    
            
            # Convert the lists to df
            data_df = pd.DataFrame(data, columns=columns)
            clm_data_df = pd.DataFrame(clm_data, columns=clm_columns)
            snw_data_df = pd.DataFrame(snw_data, columns=snw_columns)
            
            # Concatenate the df 
            output_df = pd.concat([data_df, clm_data_df, snw_data_df], axis = 1)
            
    return output_df

def FisClean(fis_df):
    
    """ Cleans up FIS results data frame including performing cloud and snow masking
    
    Parameters
    -----------
    fis_df : pandas DF
        df containing raw FIS results

    Returns
    -----------
    fis_df_clean : pandas DF
        DF containing cleaned results
    
    """
    # Import functions
    import pandas as pd
    
    # Convert stats values from objects to float
    fis_df['min'] = fis_df['min'].astype(float, errors = 'raise')
    fis_df['max'] = fis_df['max'].astype(float, errors = 'raise')
    fis_df['mean'] = fis_df['mean'].astype(float, errors = 'raise')
    fis_df['stDev'] = fis_df['stDev'].astype(float, errors = 'raise')
    fis_df['clm_mean'] = fis_df['clm_mean'].astype(float, errors = 'raise')
    fis_df['snw_mean'] = fis_df['snw_mean'].astype(float, errors = 'raise')

    # Drop rows with NaN
    fis_df.dropna(inplace=True)

    # Remove cloudy results
    fis_df.drop(fis_df[fis_df['clm_mean'] > 0].index, inplace = True)
    
    # Remove snowy results
    fis_df.drop(fis_df[fis_df['snw_mean'] > 0].index, inplace = True)

    # Format the date field
    fis_df['date'] = pd.to_datetime(fis_df['date'])

    # Average over multipolygon VMU's
    fis_df = fis_df.groupby(['date', 'ID']).mean()

    # Sort by date
    fis_df.sort_values(['ID','date'], inplace=True)

    # Reset index
    fis_df.reset_index(inplace=True)
    fis_df.set_index('date', inplace=True)
    
    return fis_df


def EvalScripts(name):
    """ Provides SentinelHub eval scripts for the following sensors/algorithms:
    Sentinel_2_NDVI, Landsat_8_NDVI
    
    Parameters
    -----------
    name : string
        name of sensor and algorithm

    Returns
    -----------
    evalscript : string
        string containing SentinelHub eval script
    
    """
    
    if name == 'Sentinel_2_NDVI':
        evalscript = """
        //VERSION=3
        function setup() {
          return {
            input: ["B04", "B08", "CLM", "SNW"],
            output: {bands: 3, sampleType: "FLOAT32"}
          }
        }

        function evaluatePixel(sample) {
          return [[(sample.B08-sample.B04)/(sample.B08+sample.B04)], sample.CLM, sample.SNW];
        }
        """
        return evalscript
        
    elif name == 'Landsat_8_NDVI':
        evalscript = """
        //VERSION=3
        function setup() {
          return {
            input: ["B03", "B04", "B05", "B06", "BQA"],
            output: {bands: 3, sampleType: "FLOAT32"}
          }
        }

        function evaluatePixel(sample) {
          return [[(sample.B05-sample.B04)/(sample.B05+sample.B04)], [decodeLs8Qa(sample.BQA).cloud],
              [(sample.B03-sample.B05)/(sample.B03+sample.B06)]];
        }
        """
        return evalscript
    
    else:
        print("No eval script found")

def GeoseriesBbox(aoi_geoseries):
    """ Creates SentinelHub BBOX object for geoseries
    
    Parameters
    -----------
    aoi_geoseries : geopandas series geometry object
        gdf with polygons in WGS84

    Returns
    -----------
    AOI_bbox : SentinelHub BBOX
        BBOX object
    
    """
    import geopandas as gpd
    from sentinelhub import BBox, CRS 
    
    # Check if input is geoseries
    if isinstance(aoi_geoseries, gpd.geoseries.GeoSeries) == True:
    
        # Get the bounding from the geoseries
        AOI_coords = list(aoi_geoseries.bounds)

        # Round up the coordinates
        AOI_coords_rounded = [round(num, 4) for num in AOI_coords]

        # Create the SentinelHub BBox object
        AOI_bbox = BBox(bbox=AOI_coords_rounded, crs=CRS.WGS84)

        return AOI_bbox
    
    else:
        print('Input is not a geopandas geoseries')