import numpy as np

def moving_average(signal, window_size):
    
    n = len(signal)
    k = (window_size - 1) // 2
    
    # output array of same length
    result = np.zeros(n, dtype=float)

    # loop through all values
    for i in range(n):
        
        # define window boundries
        start = max(0, i-k)
        end = min(n-1, i+k)
        
        #compute avg of windown
        window_values = signal[start : end + 1]
        avg = np.mean(window_values)
        
        #store in result
        result[i] = avg
        
    return result
