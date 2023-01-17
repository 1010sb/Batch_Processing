FROM python:3.8

COPY main.py /app/
COPY config.py /app/
COPY create_table.py /app/
COPY data_in_batches.py /app/
COPY test.csv /app/

RUN pip install pandas requests

WORKDIR /app
CMD ["python", "/app/main.py"]
