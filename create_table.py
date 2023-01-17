import requests
from config import table_name

def create_table():
    # Use the table_name variable in the CREATE TABLE query
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} 
          (
          ts TIMESTAMP,
          device STRING,
          co FLOAT,
          humidity FLOAT,
          light BOOLEAN,
          lpg FLOAT,
          motion BOOLEAN,
          smoke FLOAT,
          temp FLOAT
          )
          TIMESTAMP(ts)
          PARTITION BY HOUR;"""
    
    response = requests.post("http://questdb:9000/exec?query=" + query)
    
    
    if response.status_code != 200:
        print(f"Error creating table: {response.text}")
            
    else:
        print(f"Table {table_name} created successfully")


