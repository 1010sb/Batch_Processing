# Batch_Processing
In this project, I will be using telemetry data and exploring how to perform batch processing using Python and a distributed database system, such as QuestDB. I will be dividing the dataset into smaller batches and processing them separately, in order to handle large amounts of data efficiently. By the end of this project, I will have a better understanding of how to use batch processing to efficiently manage and analyze large datasets using Python and a distributed database system.

## To build the images and start the containers 
### Use the -d flag to start the containers in the background

To run the Docker Compose file, make sure that the Docker daemon is running 
on your machine and navigate to the directory where the docker-compose.yml 
file is located then run the following command:

- § docker-compose up -d

By running the command "docker-compose up", a docker image will be created for the QuestDB container and python script container as well. You can verify the launch of QuestDB container by typing "localhost:9000" in your browser, where you will be able to see the QuestDB's web-based query editor.

### Docker Image
![docker_image](https://user-images.githubusercontent.com/96765388/212904467-682e33b7-b9cc-4e59-a184-9f618d430095.JPG)

### Docker Containers
![docker_containers](https://user-images.githubusercontent.com/96765388/212904503-b1ab5be4-6fdd-4792-99bb-70f8ac997d70.JPG)

### QuestDB on Localhost:9000
![QuestDB_localhost](https://user-images.githubusercontent.com/96765388/212904536-d1748d1f-f9d1-4ab5-b753-6ed3cdb7b4a0.JPG)


## To insert data in batches
### Start only the python container. The python script container will perform the necessary data transformation and loading into QuestDB.

- § docker-compose up python
### Inserting Data in Batches
![docker_python](https://user-images.githubusercontent.com/96765388/212905771-a5fba502-4fa8-417e-95ed-982ad2cd6b03.JPG)

### By refreshing the page at 'localhost:9000' and running the command 'select * from test', you will see that the data has been successfully transferred.
![data_questdb](https://user-images.githubusercontent.com/96765388/212906725-e7875cde-6ecd-4b58-8219-b70f82569c70.JPG)


## To stop the questdb containers 
- § docker stop questdb

## Start only the QuestDB container
- § docker-compose up questdb

## To stop the containers and remove them, Use the following command
- § docker-compose down
