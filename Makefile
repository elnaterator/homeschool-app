.DEFAULT_GOAL := help
.PHONY: help up exec stop test

up: ## Build and run app in docker containers
	poetry lock --no-update
	poetry export -f requirements.txt --output requirements.txt --without-hashes
	docker compose up --build

bash: ## Run bash in the web docker container
	docker compose exec web sh -c /bin/bash

stop: ## Stop the docker container
	docker compose down

test: ## Run the tests
	docker compose run --rm web pytest

help: ## Print these help docs
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
