build:
	docker build -t flask-sample:latest .
stop:
	docker stop myFlask
rm-container:
	docker rm myFlask
rm-image:
	docker rmi flask-sample:latest
clean:docker-stop docker-delc docker-deli
run:
	docker run -p 4000:4000 -v E:\Development\python\restfulFlask\.env:/app/.env --name myFlask flask-sample
