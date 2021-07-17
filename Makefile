.DEFAULT_GOAL := help
.PHONY: coverage deps help lint publish push test tox

build: ## Build docker compose
	sudo docker-compose build

up: ## Build docker compose
	sudo docker-compose up

# tox:  ## Run automatic tests on webapi
# 	python -m tox
# 	ls -la

coverage: ## Check test coverage files
	coverage run --source=webapi/

format: ## Formats by company code style
	flake8 webapi/

help:  ## Show help message
	echo "Help"