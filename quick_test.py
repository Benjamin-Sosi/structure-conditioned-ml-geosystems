import pandas as pd
from representation import partition_by_domain
from feature_engineering import construct_features
from learning import train_model
from validation import convergence_validation

# Load dataset
df = pd.read_csv("synthetic_dataset.csv")

# Partition by structural regime
domains = partition_by_domain(df)

results = {}

for domain_id, domain_df in domains.items():
    
    # Feature construction
    X, y = construct_features(domain_df)
    
    # Train model within domain
    model = train_model(X, y)
    
    # Predict
    predictions = model.predict(X)
    
    # Convergence validation
    score = convergence_validation(predictions, domain_df["geological_indicator"])
    
    results[domain_id] = score

print("Structure-conditioned workflow executed successfully.")
print("Convergence scores by domain:")
print(results)
