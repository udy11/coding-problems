import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError('List must contain nine numbers.')
    mat = np.reshape(lst, (3, 3))
    return {'mean' : [list(np.mean(mat, axis = 0)), list(np.mean(mat, axis = 1)), np.mean(lst)],
            'variance' : [list(np.var(mat, axis = 0)), list(np.var(mat, axis = 1)), np.var(lst)],
            'standard deviation' : [list(np.std(mat, axis = 0)), list(np.std(mat, axis = 1)), np.std(lst)],
            'max' : [list(np.max(mat, axis = 0)), list(np.max(mat, axis = 1)), np.max(lst)],
            'min' : [list(np.min(mat, axis = 0)), list(np.min(mat, axis = 1)), np.min(lst)],
            'sum' : [list(np.sum(mat, axis = 0)), list(np.sum(mat, axis = 1)), np.sum(lst)]}
