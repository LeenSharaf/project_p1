 FROM ubuntu:latest
 WORKDIR /home/front-end

 # Install dependencies
 RUN apt-get update -y
 RUN apt-get install -y python3 python3-pip nano gcc

#Install Flask
 RUN pip3 install flask requests
# Copy 
 COPY frontend.py ./

 EXPOSE 5000

 CMD ["python3", "./frontend.py"]
