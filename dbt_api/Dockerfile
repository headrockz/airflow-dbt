FROM ghcr.io/dbt-labs/dbt-postgres:1.2.latest

USER root
WORKDIR /dbt

RUN pip install Flask
ENV FLASK_APP=app.py

EXPOSE 8080

ENTRYPOINT [ "python", "app.py" ]