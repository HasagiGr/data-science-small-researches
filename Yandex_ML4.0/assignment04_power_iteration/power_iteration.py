import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps

    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HEREr
    v = np.random.rand(data.shape[1])
    
    for _ in range(num_steps):
        v = np.dot(data, v)  
        v /= np.linalg.norm(v)  

    eigenvalue = float(np.dot(np.dot(data, v), v) / np.dot(v, v))

    return eigenvalue, v