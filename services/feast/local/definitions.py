from datetime import timedelta
from feast import (
    Entity,
    FeatureService,
    FeatureView,
    Field,
    FileSource,
    PushSource,
    RequestSource
)
from feast.infra.offline_stores.contrib.postgres_offline_store.postgres_source import PostgreSQLSource
from feast.on_demand_feature_view import on_demand_feature_view
from feast.types import Float32, Float64, Int32, Int64, String, Bytes, Bool, UnixTimestamp

# Entity defined by kfp-component, do not change here. 
event_timestamp = Entity(name="event_timestamp", join_keys=["event_timestamp"])
        
# Source defined by kfp-component, do not change here. 
new_zealand_statistical_areas____generalised_src = PostgreSQLSource(
    name="new zealand statistical areas -- generalised_sql",
    query="SELECT * FROM new_zealand_statistical_areas____generalised",
    # query="new_zealand_statistical_areas____generalised",
    timestamp_field="event_timestamp"
)
        
# Feature View defined by kfp-component, do not change here. 
new_zealand_statistical_areas____generalised_fv = FeatureView(
    name="new_zealand_statistical_areas____generalised",
    entities=[event_timestamp],
    ttl=timedelta(days=1),
    schema=[  
        Field(name="field_name_1", dtype=String),
        Field(name="field_name_2", dtype=String),
        Field(name="field_name_3", dtype=String),
        Field(name="field_name_4", dtype=String),
        Field(name="field_name_5", dtype=String),
        Field(name="field_name_6", dtype=String),
        Field(name="field_name_7", dtype=String),
        Field(name="field_name_8", dtype=String),
        Field(name="field_name_8", dtype=String)
    ],
    online=True,
    source=new_zealand_statistical_areas____generalised_src
)
        
# Source defined by kfp-component, do not change here. 
new_zealand_business_demography_statistics_src = PostgreSQLSource(
    name="new zealand business demography statistics_sql",
    query="SELECT * FROM new_zealand_business_demography_statistics",
    # query="new_zealand_business_demography_statistics",
    timestamp_field="event_timestamp"
)
        
# Feature View defined by kfp-component, do not change here. 
new_zealand_business_demography_statistics_fv = FeatureView(
    name="new_zealand_business_demography_statistics",
    entities=[event_timestamp],
    ttl=timedelta(days=1),
    schema=[  
        Field(name="field_name_1", dtype=String),
        Field(name="field_name_2", dtype=String),
        Field(name="field_name_3", dtype=String),
        Field(name="field_name_4", dtype=String),
        Field(name="field_name_4", dtype=String)
    ],
    online=True,
    source=new_zealand_business_demography_statistics_src
)
        
# Feature Set defined by kfp-component, do not change here. 
# sweetas_economic_features_fs = FeatureService(
#    name="sweetas_economic_features",
#    features=['new_zealand_statistical_areas____generalised_fv', 'new_zealand_business_demography_statistics_fv']
# )
