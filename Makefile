
BUILD_MODE	:= build  ## Pass `pull` in order to pull images instead of building them
NAME		:= footyhints
NO_CACHE	:= ## Pass `--no-cache` in order to disable Docker cache
PARALLEL	:= --parallel

run:
	docker-compose -f docker-compose.yml -p footyhints up -d

build:
	docker-compose -f docker-compose.yml -p footyhints build base
	docker-compose -f docker-compose.yml -p footyhints build --parallel

stop:
	docker-compose -f docker-compose.yml -p footyhints stop

rebuild: build stop run

.PHONY: tests
tests: build-tests run-tests  ## Run all tests (getting/building images as needed)

.PHONY: build-tests
build-tests:  ## Build end-to-end test environment only
	docker-compose -f docker/docker-compose-tests.yml -p test-$(NAME) $(NO_CACHE) $(BUILD_MODE) base
	docker-compose -f docker/docker-compose-tests.yml -p test-$(NAME) $(NO_CACHE) $(BUILD_MODE)

.PHONY: run-tests
run-tests: ## Just run the tests (no build/get). Use `make TEST_CASE=tests/...` for specific tests only
	#docker run -it --rm test-footyhints_tester bash -c "source /opt/footyhints/envs/python/bin/activate && flake8 --config .flake8 ./"
	docker run -it --rm --network=test-footyhints_default test-footyhints_tester bash -c "source /opt/footyhints/envs/python/bin/activate && py.test tests"
