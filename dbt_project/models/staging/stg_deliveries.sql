with raw_data as (
    select * from read_json_auto('../downloads/dataset_*.json')
)

select
    id as delivery_id,
    cast(created_at as timestamp) as created_at,
    cast(deadline as timestamp) as deadline,
    cast(delivered_at as timestamp) as delivered_at,
    origin,
    destination,
    driver_id,
    vehicle_id,
    status as raw_status
from raw_data
