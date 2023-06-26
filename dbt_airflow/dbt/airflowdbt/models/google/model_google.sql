with base as (
  select 
    date_close,
    low::NUMERIC(30,2),
    high::NUMERIC(30,2),
    open::NUMERIC(30,2),
    close::NUMERIC(30,2),
    (open - close)::NUMERIC(30,2) as diff_open_close,
    (high - low)::NUMERIC(30,2) as diff_high_low
  from {{source('sources', 'google')}}
)
 
select * from  base