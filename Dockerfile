# Use an official Python runtime as a parent image
FROM python:3.8.10

# Set the working directory in the container to /usr/src/app
WORKDIR /usr/src/app

# Add requirements file to the working directory
ADD requirements.txt /usr/src/app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Supervisor
RUN apt-get update && apt-get install -y supervisor

# Para os logs da nossa aplicação
RUN mkdir -p /var/log/airflow/

# Create airflow directory
RUN mkdir -p /root/airflow/

# Create airflow dags directory
RUN mkdir -p /root/airflow/dags

# Add the airflow configuration file
ADD airflow.cfg /root/airflow/

# Add the script that will start Airflow services
ADD airflow.sh /usr/src/app/

# Add the dags from your host to the container
ADD /crawler /root/airflow/dags

RUN airflow db init

RUN airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com --password admin

# # Give execution rights to the script
# RUN chmod +x /usr/src/app/airflow.sh

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Add the Supervisor configuration file
ADD supervisor.conf /etc/supervisor/conf.d/supervisor.conf

# Run the script when the container launches
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisor.conf"]
