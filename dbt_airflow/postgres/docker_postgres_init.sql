CREATE DATABASE finance;

CREATE TABLE apple (
    date_close date,
    open numeric(30, 6),
    high numeric(30, 6),
    low numeric(30, 6),
    close numeric(30, 6),
    volume bigint
);
CREATE TABLE google (
    date_close date,
    open numeric(30, 6),
    high numeric(30, 6),
    low numeric(30, 6),
    close numeric(30, 6),
    volume bigint
);