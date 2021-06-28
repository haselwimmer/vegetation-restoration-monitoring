def GeeArrayToDf(arr, list_of_bands):
    
    """ Transforms client-side ee.Image.getRegion array to pandas.DataFrame
    
    Parameters
    -----------
    arr : list
        list of GEE array items
    
    list_of_bands:
        list of bands in returned GEE array to iterate over

    Returns
    -----------
    df : pandas dataframe
        Pandas df containing reformatted GEE results
    
    """
    
    # Import functions
    import pandas as pd
    
    df = pd.DataFrame(arr)

    # Rearrange the header.
    headers = df.iloc[0]
    df = pd.DataFrame(df.values[1:], columns=headers)

    # Remove rows without data inside.
    df = df[['longitude', 'latitude', 'time', *list_of_bands]].dropna()

    # Convert the data to numeric values.
    for band in list_of_bands:
        df[band] = pd.to_numeric(df[band], errors='coerce')

    # Convert the time field into a datetime.
    df['datetime'] = pd.to_datetime(df['time'], unit='ms')

    # Keep the columns of interest.
    df = df[['time','datetime',  *list_of_bands]]

    return df