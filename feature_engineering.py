import pandas as pd

def construct_features(df):
    """
    Transform raw attributes into physics-consistent features.
    Example: combine fracture intensity and resistivity
    into a structural connectivity proxy.
    """
    df = df.copy()
    
    # Example derived feature
    df["connectivity_index"] = df["fracture_intensity"] / (df["resistivity"] + 1e-6)
    
    return df[["connectivity_index"]], df["hydraulic_response"]

