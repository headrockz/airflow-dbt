FROM apache/airflow:2.6.2-python3.11

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         build-essential gcc python3-dev \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
RUN chown -R airflow:root /opt/airflow
USER airflow
COPY ./airflow/requirements.txt requirements.txt
RUN pip install --no-cache-dir --user -r requirements.txt --no-warn-script-location