import numpy as np

def convergence_validation(predictions, geological_indicator):
    """
    Assess consistency between ML predictions
    and independent geological constraint.
    """
    correlation = np.corrcoef(predictions, geological_indicator)[0, 1]
    return correlation
