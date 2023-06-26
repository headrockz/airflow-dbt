#!/bin/sh
dbt deps --profiles-dir .  # Pulls the most recent version of the dependencies listed in your packages.yml from git
dbt debug --target dev --profiles-dir .
dbt run --select $1 --target dev --profiles-dir .