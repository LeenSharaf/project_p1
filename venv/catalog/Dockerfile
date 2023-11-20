FROM ubuntu:latest
WORKDIR /home/catalog
# Install dependencies
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip nano gcc
# Install Flask 
RUN pip3 install flask requests
# Copy 
COPY catalog.py ./
## Port
EXPOSE 5001
#Run application
CMD ["python3", "./catalog.py"]
