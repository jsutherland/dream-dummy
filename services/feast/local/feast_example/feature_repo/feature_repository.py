# This is an example feature definition file

from datetime import timedelta
from feast.infra.offline_stores.contrib.postgres_offline_store.postgres_source import (
    PostgreSQLSource,
)
from feast import (
    Entity,
    FeatureService,
    FeatureView,
    Field
)
from feast.on_demand_feature_view import on_demand_feature_view
from feast.types import Float32, Float64, Int64

# Define entity
date = Entity(name="event_timestamp", join_keys=["event_timestamp"])

# Define sources
corestickm159sfrbatl_src = PostgreSQLSource(
    name="corestickm159sfrbatl",
    query="SELECT * FROM corestickm159sfrbatl",
    timestamp_field="event_timestamp",
)

gdp_src = PostgreSQLSource(
    name="gdp",
    query="SELECT * FROM gdp",
    timestamp_field="event_timestamp",
)

usacpicorminmei_src = PostgreSQLSource(
    name="usacpicorminmei",
    query="SELECT * FROM usacpicorminmei",
    timestamp_field="event_timestamp",
)

wm1ns_src = PostgreSQLSource(
    name="wm1ns",
    query="SELECT * FROM wm1ns",
    timestamp_field="event_timestamp",
)

m1v_src = PostgreSQLSource(
    name="m1v",
    query="SELECT * FROM m1v",
    timestamp_field="event_timestamp",
)

# Define feature view
corestickm159sfrbatl_fv = FeatureView(
    name="corestickm159sfrbatl",
    entities=[date],
    ttl=timedelta(days=1),
    schema=[
        Field(name="value", dtype=Float32)
    ],
    online=True,
    source=corestickm159sfrbatl_src
)

gdp_fv = FeatureView(
    name="gdp",
    entities=[date],
    ttl=timedelta(days=1),
    schema=[
        Field(name="value", dtype=Float32)
    ],
    online=True,
    source=gdp_src
)

usacpicorminmei_fv = FeatureView(
    name="usacpicorminmei",
    entities=[date],
    ttl=timedelta(days=1),
    schema=[
        Field(name="value", dtype=Float32)
    ],
    online=True,
    source=usacpicorminmei_src
)

wm1ns_fv = FeatureView(
    name="wm1ns",
    entities=[date],
    ttl=timedelta(days=1),
    schema=[
        Field(name="value", dtype=Float32)
    ],
    online=True,
    source=wm1ns_src
)

m1v_fv = FeatureView(
    name="m1v",
    entities=[date],
    ttl=timedelta(days=1),
    schema=[
        Field(name="value", dtype=Float32)
    ],
    online=True,
    source=m1v_src
)


# Define feature service
usecase_v1 = FeatureService(
    name="usecase_v1",
    features=[
        usacpicorminmei_fv,
        gdp_fv,
        corestickm159sfrbatl_fv,
        wm1ns_fv,
        m1v_fv
    ]
)