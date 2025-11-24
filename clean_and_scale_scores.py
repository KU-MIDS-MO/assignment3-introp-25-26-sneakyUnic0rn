import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
    
    #create a copy to make changes
    copy = np.array(scores)
    
    #for 1D array
    if copy.ndim == 1:
        for i in range(len(copy)):
            if copy[i] < min_score:
                copy[i] = min_score
            if copy[i] > max_score:
                copy[i] = max_score

    #for 2D array   
    else:            
        for row in range(copy.shape[0]):                #copy.shape[0] for row
            for col in range(copy.shape[1]):            #copy.shape[1] for column
                if copy[row, col] < min_score:
                    copy[row, col] = min_score 
                if copy[row, col] > max_score: 
                    copy[row, col] = max_score
                    
    scaled = (copy - min_score) / (max_score - min_score)
    
    return scaled