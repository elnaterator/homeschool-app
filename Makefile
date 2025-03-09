.DEFAULT_GOAL := help
.PHONY: help up exec stop test

BUILD_FLAG := $(if $(build),--build,)

up: ## Build and run app in docker containers
	poetry lock --no-update
	poetry export -f requirements.txt --output requirements.txt --without-hashes
	docker compose up $(BUILD_FLAG)

bash: ## Run bash in the web docker container
	docker compose exec web sh -c /bin/bash

stop: ## Stop the docker container
	docker compose down

test: ## Run the tests
	poetry export -f requirements.txt --output requirements.txt --without-hashes --with dev
	docker compose run --rm $(BUILD_FLAG) web pytest

makemigrations: ## Create django db migrations
	docker compose run --rm $(BUILD_FLAG) web python manage.py makemigrations

migrate: ## Run django db migrations
	docker compose run --rm $(BUILD_FLAG) web python manage.py migrate

rollback: ## Rollback django db migrations
	docker compose run --rm $(BUILD_FLAG) web python manage.py migrate --fake

shell: ## Run django shell
	docker compose run --rm $(BUILD_FLAG) web python manage.py shell

help: ## Print these help docs
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
