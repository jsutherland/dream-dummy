from feast import FeatureStore
import pandas as pd
from datetime import datetime
from feast.infra.offline_stores.contrib.postgres_offline_store.postgres_source import (
    PostgreSQLSource,
    SavedDatasetPostgreSQLStorage
)

store = FeatureStore(repo_path="./feature_repo")

# Return features example
feature_store = FeatureStore(repo_path='./feature_repo')

table = "_dates"

entity_sql = f"""
    SELECT event_timestamp
    FROM {table}
"""

training_df = feature_store.get_historical_features(
    entity_df=entity_sql,
    full_feature_names=True,
    features=[
        "gdp:value",
        "corestickm159sfrbatl:value",
        "usacpicorminmei:value",
        "wm1ns:value",
        "m1v:value"
    ],
).to_df().dropna()


pd.set_option('display.max_rows', 10)
print(training_df)
