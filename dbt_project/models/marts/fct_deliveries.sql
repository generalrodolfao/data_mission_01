with staging as (
    select * from {{ ref('stg_deliveries') }}
)

select
    *,
    {{ get_delivery_priority('deadline', 'now()') }} as priority,
    {{ get_delivery_status('delivered_at', 'deadline') }} as status,
    datediff('minute', deadline, delivered_at) as delay_minutes
from staging
