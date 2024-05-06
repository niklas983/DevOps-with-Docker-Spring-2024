# Start from the ubuntu image 
FROM ubuntu:22.04

# instructions will be executed in this location
WORKDIR /home/nik/DevOpsDocker

# Copy the script file into the container
COPY script.sh .

# add execution permissions during the build.
RUN chmod +x script.sh

# Execute command to update ubuntu
RUN apt-get update

# Execute command to install curl
RUN apt-get -y install curl

# When running Docker run the command will be ./script.sh
CMD ./script.sh

