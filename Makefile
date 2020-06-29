
BUILD_MODE	:= build  ## Pass `pull` in order to pull images instead of building them
NAME		:= footyhints
NO_CACHE	:= ## Pass `--no-cache` in order to disable Docker cache
PARALLEL	:= --parallel

HASH    := $$(git log -1 --pretty=%h)
RELEASE_TAG := $$(git describe --abbrev=0 --tags)
RELEASE_VERSION := $(filter-out 'v',$(RELEASE_TAG))

IMAGES := nginx base bootstrap flask cron

.PHONY:all
all:
	@echo $(RELEASE_VERSION)
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

## RELEASES ##
REGISTRY := footyhints

.PHONY: login-dockerhub
login-dockerhub: ## Login to DockerHub
	@echo "Logging into dockerhub"
	@echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" --password-stdin

.PHONY: update-remote-tags
update-remote-tags: ## Ensure local git has most recent tags
	git fetch --all --tags

.PHONY: build-release-images
build-release-images: ## Build release images with latest and newest tag
	@echo "Building release images for latest and ${RELEASE_TAG} with registry: ${REGISTRY}"
	@for image in $(IMAGES); do \
		docker build -f docker/$$image/Dockerfile -t ${REGISTRY}/$$image:latest -t ${REGISTRY}/$$image:${RELEASE_TAG} .; \
	done

.PHONY: push-release-images
push-release-images: ## Push release images with latest and newest tag
	@echo "Pushing release images for latest and ${RELEASE_TAG} to registry: ${REGISTRY}"
	@for image in $(IMAGES); do \
		docker push ${REGISTRY}/$$image:latest
		docker push ${REGISTRY}/$$image:${RELEASE_TAG}
	done
