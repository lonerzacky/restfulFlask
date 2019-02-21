LOCAL_DESTINATION=E:\Development\python\restfulFlask\

build:
	docker build -t flask-app:latest .
stop:
	docker stop myFlask
rm-container:
	docker rm myFlask
rm-image:
	docker rmi flask-app:latest
clean:
	docker stop myFlask && docker rm myFlask && docker rmi flask-sample:latest
run:
	docker run -p 4000:4000 -v ${LOCAL_DESTINATION}.env:/app/.env --name myFlask flask-app
env-init:
	cp .env.example .env