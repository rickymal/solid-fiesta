# docker rm my_airflow_container
# docker build -t my-airflow-image . 
# docker run -it -p 8080:8080 --name my_airflow_container my-airflow-image

docker-compose up --build -d
docker-compose up -d
docker-compose ps
docker-compose down
