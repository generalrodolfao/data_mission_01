{% macro get_delivery_priority(deadline, current_time) %}
    case
        when {{ deadline }} < {{ current_time }} then 'CRITICAL'
        when datediff('hour', {{ current_time }}, {{ deadline }}) <= 2 then 'HIGH'
        when datediff('hour', {{ current_time }}, {{ deadline }}) <= 5 then 'MEDIUM'
        else 'LOW'
    end
{% endmacro %}

{% macro get_delivery_status(delivered_at, deadline) %}
    case
        when {{ delivered_at }} is not null and {{ delivered_at }} <= {{ deadline }} then 'DELIVERED_ON_TIME'
        when {{ delivered_at }} is not null and {{ delivered_at }} > {{ deadline }} then 'DELIVERED_LATE'
        when {{ delivered_at }} is null and now() > {{ deadline }} then 'OVERDUE'
        else 'PENDING'
    end
{% endmacro %}
