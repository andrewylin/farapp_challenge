Before starting, please make sure you have Docker installed and running
https://www.docker.com/get-docker

Build the image (replace <YOUR_USERNAME> with your Docker Cloud username):
$ docker build -t <YOUR_USERNAME>/farapp_challenge .

Run the image using: 
$ docker run -p 8888:5000 --name farapp_challenge <YOUR_USERNAME>/farapp_challenge

The website:
http://localhost:8888

Please refer to https://github.com/docker/labs/blob/master/beginner/chapters/webapps.md for more information on building and running Docker images
