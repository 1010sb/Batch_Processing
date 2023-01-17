import csv
import requests
import datetime
from config import table_name, csv_file


def data_in_batches():
    # Read the data from the CSV file
    with open(csv_file, 'r') as f:

        reader = csv.reader(f)
        # Skip the first row (column names)
        next(reader)
        # Read the data rows
        rows = [row for row in reader]

    # Convert the 'ts' column to a timestamp and the 'temp' column to Celsius
    for row in rows:

        row[0] = datetime.datetime.fromtimestamp(float(row[0]))
        row[8] = (float(row[8]) - 32) * 5 / 9


    batch_size = 350

    # Calculate the number of batches
    num_batches = len(rows) // batch_size + (len(rows) % batch_size > 0)


    # Insert the data into the QuestDB table in batches of rows

    for i, batch in enumerate(range(0, len(rows), batch_size)):

        batch_number = i+1

        batch = rows[i:i+batch_size]
        
        values = ", ".join([f"('{row[0]}', '{row[1]}', {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]})" for row in batch])
        
        query = f"INSERT INTO {table_name} (ts, device, co, humidity, light, lpg, motion, smoke, temp) VALUES {values}"
        
        response = requests.post("http://questdb:9000/exec?query=" + query)
        

        # Check the response status code and handle the response accordingly
        if response.status_code != 200:
            print(f"Batch {batch_number} of {num_batches} Error Inserting Data: {response.text}")

        else:
            print(f"Batch {batch_number} of {num_batches} Inserted Successfully")
