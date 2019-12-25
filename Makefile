
BUILD_MODE	:= build  ## Pass `pull` in order to pull images instead of building them
NAME		:= footyhints
NO_CACHE	:= ## Pass `--no-cache` in order to disable Docker cache
PARALLEL	:= --parallel

HASH    := $$(git log -1 --pretty=%h)
IMAGES := nginx base bootstrap flask cron

.PHONY:all
all:
	@echo 'Available make targets:'
	@grep '^[^#[:space:]^\.PHONY.*].*:' Makefile


run: ## Run the full docker stack
	docker-compose -f docker/docker-compose.yml -p $(NAME) up -d

build: ## Build the full docker stack
	docker-compose -f docker/docker-compose.yml -p $(NAME) $(BUILD_MODE) base
	docker-compose -f docker/docker-compose.yml -p $(NAME) $(BUILD_MODE) --parallel

stop: ## Stop the full docker stack
	docker-compose -f docker/docker-compose.yml -p $(NAME) stop

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
	docker run -it --rm --env-file=docker/tests.env -v artifacts:/opt/footyhints/envs/artifacts/ --network=footyhints_default footyhints/tester

.PHONY: release-latest-images
release-latest-images: build ## Push images to dockerhub
	@echo "Logging into dockerhub"
	@echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" --password-stdin
	@for image in $(IMAGES); do \
		docker tag footyhints/$$image:latest footyhints/$$image:${HASH}; \
		docker push footyhints/$$image:latest; \
		docker push footyhints/$$image:${HASH}; \
	done
