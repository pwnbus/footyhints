
BUILD_MODE	:= build  ## Pass `pull` in order to pull images instead of building them
NAME		:= footyhints
NO_CACHE	:= ## Pass `--no-cache` in order to disable Docker cache
PARALLEL	:= --parallel

run:
	docker-compose -f docker-compose.yml -p $(NAME) up -d

build:
	docker-compose -f docker-compose.yml -p $(NAME) build base
	docker-compose -f docker-compose.yml -p $(NAME) build --parallel

stop:
	docker-compose -f docker-compose.yml -p $(NAME) stop

rebuild: build stop run

.PHONY: tests
tests: build-tests run-tests  ## Run all tests (getting/building images as needed)

.PHONY: build-tests
build-tests:  ## Build end-to-end test environment only
	docker-compose -f docker/docker-compose-tests.yml -p $(NAME) $(NO_CACHE) $(BUILD_MODE) base
	docker-compose -f docker/docker-compose-tests.yml -p $(NAME) $(NO_CACHE) $(BUILD_MODE)

.PHONY: run-tests-resources-external
run-tests-resources-external: ## Just spin up external resources for tests and have them listen externally
	docker-compose -f docker/docker-compose-tests.yml -p $(NAME) run -p 3306:3306 -d mysql

.PHONY: run-tests-resources
run-tests-resources:  ## Just run the external resources required for tests
	docker-compose -f docker/docker-compose-tests.yml -p $(NAME) up -d

.PHONY: run-tests
run-tests: run-tests-resources ## Run testing suite
	docker run -it --rm footyhints/tester bash -c "flake8 --config .flake8 ./"
	docker run -it --rm --network=footyhints_default footyhints/tester
