FROM ubuntu:latest
 WORKDIR /home/order

 # Install dependencies
 RUN apt-get update -y
 RUN apt-get install -y python3 python3-pip nano gcc
# Install Flask
 RUN pip3 install flask requests
# Copy
 COPY order.py ./
 EXPOSE 5002
 CMD ["python3", "./order.py"]
