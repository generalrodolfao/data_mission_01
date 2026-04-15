{% macro get_delivery_priority(deadline_col, current_time_expr='now()') %}
    case
        when {{ deadline_col }} < {{ current_time_expr }} then 'CRITICAL'
        when datediff('hour', {{ current_time_expr }}, {{ deadline_col }}) <= 2 then 'HIGH'
        when datediff('hour', {{ current_time_expr }}, {{ deadline_col }}) <= 5 then 'MEDIUM'
        else 'LOW'
    end
{% endmacro %}

{% macro get_delivery_status(delivered_at_col, deadline_col, current_time_expr='now()') %}
    case
        when {{ delivered_at_col }} is not null and {{ delivered_at_col }} <= {{ deadline_col }} then 'DELIVERED_ON_TIME'
        when {{ delivered_at_col }} is not null and {{ delivered_at_col }} > {{ deadline_col }} then 'DELIVERED_LATE'
        when {{ delivered_at_col }} is null and {{ current_time_expr }} > {{ deadline_col }} then 'OVERDUE'
        else 'PENDING'
    end
{% endmacro %}
