import pandas as pd

def partition_by_domain(df):
    """
    Partition dataset into connectivity-controlled structural regimes.
    Returns dictionary of domain_id -> dataframe.
    """
    domains = {}
    for domain in df["domain_id"].unique():
        domains[domain] = df[df["domain_id"] == domain].copy()
    return domains
