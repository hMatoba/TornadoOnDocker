docker build -t tor_app ./
docker run -d -p 80:80 --name tor_tmp tor_app
