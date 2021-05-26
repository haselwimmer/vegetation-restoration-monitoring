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

def EvalScripts(name):
    """ Provides eval scripts for common algorithms + sensors
    
    Parameters
    -----------
    name : string
        name of algorithm and sensor

    Returns
    -----------
    evalscript : string
        string containing SentinelHub eval script
    
    """
    
    if name == 'Sentinel_2_NDVI':
        evalscript = 'return [[(B08 - B04) / (B08 + B04)], CLM, SNW]'
    
    elif name == 'Landsat_8_NDVI':
        #evalscript = 'return [[(B05-B04)/(B05+B04)], decodeLs8Qa(BQA).cloudConfidence, decodeLs8Qa(BQA).snowIceConfidence]'
        evalscript = 'return [(B05-B04)/(B05+B04)]'
    
    return evalscript