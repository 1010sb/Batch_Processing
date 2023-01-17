# Batch_Processing
In this project, I will be using telemetry data and exploring how to perform batch processing using Python and a distributed database system, such as QuestDB. I will be dividing the dataset into smaller batches and processing them separately, in order to handle large amounts of data efficiently. By the end of this project, I will have a better understanding of how to use batch processing to efficiently manage and analyze large datasets using Python and a distributed database system.

## To build the images and start the containers 
### Use the -d flag to start the containers in the background

To run the Docker Compose file, make sure that the Docker daemon is running 
on your machine and navigate to the directory where the docker-compose.yml 
file is located then run the following command:

§ docker-compose up -d

## To insert data in batches
### Start only the python container

§ docker-compose up python

## To stop the questdb containers 
§ docker stop questdb

## Start only the QuestDB container
§ docker-compose up questdb

## To stop the containers and remove them, Use the following command
§ docker-compose down
