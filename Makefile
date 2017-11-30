run:
	docker-compose -f docker/docker-compose.yml -p footyhints up -d

build:
	docker-compose -f docker/docker-compose.yml -p footyhints build

stop:
	docker-compose -f docker/docker-compose.yml -p footyhints stop

rebuild: build stop run
