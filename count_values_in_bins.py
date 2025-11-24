import numpy as np

def count_values_in_bins(data, bin_edges):
    
    # set number of bins
    num_bin = len(bin_edges) - 1
    
    # create output for counts
    counts = np.zeros(num_bin)
    
    # init loop for all values in data
    for value in data:
        
        # ignore outside values
        if value < bin_edges[0] or value > bin_edges[-1]:
            continue
        
        # check all bins
        for i in range(num_bin):
            left = bin_edges[i]
            right = bin_edges[i+1]
            
            # last bin is inclusive on right
            if i == num_bin - 1:
                if left <= value <= right:
                    counts[i] += 1
                    
            else:
                if left <= value < right:
                    counts[i] += 1
                    
    return counts

