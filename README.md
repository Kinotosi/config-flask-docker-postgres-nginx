# Configuration Web Dynamic with Flask Framework, Docker, PostgreSQL, and Nginx
This is about configuration web dynamics with Flask Framework basic. This web running used PostgreSQL as a database system, Nginx as a web server, and docker as a run web application.

## How to run
### Install docker
1. Open your terminal or cmd
2. Install docker and docker-compose
```
sudo apt-get install docker docker-compose
```
3. Configuration your docker
```
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```
### Run application
1. Download this file
2. Build docker-compose
```
docker-compose build
```
3. Run docker-compose
```
docker-compose up -d --build
```
## References
[https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/#postgres](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/#postgres)
