import numpy as np
def remove_outliers(x, y, threshold=3):
    """
    Removes outliers from y and the corresponding x values based on the Z-score method.

    Parameters:
    x (list or numpy array): The list or array of x values.
    y (list or numpy array): The list or array of y values.
    threshold (float): The Z-score threshold to identify outliers. Default is 3.

    Returns:
    filtered_x, filtered_y (numpy arrays): The filtered x and y values without outliers.
    """
    # Convert to numpy arrays if they are not already
    x = np.array(x)
    y = np.array(y)
    
    # Calculate the Z-scores of y
    mean_y = np.mean(y)
    std_y = np.std(y)
    z_scores = (y - mean_y) / std_y
    
    # Filter out the outliers
    mask = np.abs(z_scores) < threshold
    filtered_x = x[mask]
    filtered_y = y[mask]
    
    return filtered_x, filtered_y
