run:
	docker-compose -f docker-compose.yml -p footyhints up -d

build:
	docker-compose -f docker-compose.yml -p footyhints build base
	docker-compose -f docker-compose.yml -p footyhints build --parallel

stop:
	docker-compose -f docker-compose.yml -p footyhints stop

rebuild: build stop run
