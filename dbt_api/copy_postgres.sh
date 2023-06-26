psql -d finance -U postgres -f /files/tables.sql

psql -d finance -U postgres -c "copy apple from '/files/aapl.csv' DELIMITER ',' CSV HEADER"

psql -d finance -U postgres -c "copy google from '/files/goog.csv' DELIMITER ',' CSV HEADER "
