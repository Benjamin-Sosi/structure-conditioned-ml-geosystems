from sklearn.ensemble import RandomForestRegressor

def train_model(X, y):
    """
    Standard ML algorithm.
    No architecture modification.
    """
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X, y)
    return model
