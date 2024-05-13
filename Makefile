tests:
	echo "Running backend tests"
	poetry run .\backend\manage.py test --settings=config.settings.test_settings

.PHONY: setup install_venv install_migrations

setup: install_venv install_migrations

install_venv:
	python3 -m venv ./.venv
	. ./.venv/bin/activate
	pip install -r ./backend/requirements/requirements.txt && pip install -r ./backend/requirements/dev-requirements.txt

	@if [ -f ".env/.env.dev"]; then \
		echo ".env.dev exists; SKIP"
	else \
		touch .env/env.dev
		cp .env.example .env/dev

install_migrations:
	python3 manage.py makemigrations users
	python3 manage.py migrate


@.PHONY: docker_hardreset docker_down_volume

docker_hardreset:
	docker_down_volume
	docker system prune
	docker compose build --no-cache

docker_down_volume:
	docker compose -f development.yml down -v --rmi all
