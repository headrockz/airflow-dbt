CREATE TABLE apple (
    date_close date,
    open numeric(30, 6),
    high numeric(30, 6),
    low numeric(30, 6),
    close numeric(30, 6),
    adj_close numeric(30, 6),
    volume bigint
);
CREATE TABLE google (
    date_close date,
    open numeric(30, 6),
    high numeric(30, 6),
    low numeric(30, 6),
    close numeric(30, 6),
    adj_close numeric(30, 6),
    volume bigint
);

COPY apple from '/files/aapl.csv' DELIMITER ',' CSV HEADER;
COPY google from '/files/goog.csv' DELIMITER ',' CSV HEADER; 