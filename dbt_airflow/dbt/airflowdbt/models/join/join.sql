{{
    config(
        materialized='table'
    )
}}

with apple as(
    select * from {{ref('model_apple')}}
), google as (
    select * from {{ref('model_google')}}
)

select 
    a.date_close, 
    a.diff_high_low as apple_diff_hl, 
    a.diff_open_close as apple_diff_oc,
    g.diff_high_low as google_diff_hl, 
    g.diff_open_close as google_diff_oc
from apple as a, google as g 