.DEFAULT_GOAL := help
.PHONY: coverage deps help lint publish push test tox

build: ## Build docker compose
	sudo docker-compose build

up: ## Up docker compose
	sudo docker-compose up

run: ## Build and wake-up
	sudo docker-compose build && sudo docker-compose up


coverage: ## Check test coverage files
	coverage run --source=webapi/

format: ## Formats by company code style
	flake8 webapi/

help:  ## Show help message
	echo "To run a command execute like the example\n>>>make run"


# tox:  ## Run automatic tests on webapi
# 	python -m tox
# 	ls -la	