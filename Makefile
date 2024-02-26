tests:
	echo "Running backend tests"
	poetry run .\backend\manage.py test --settings=config.settings.test_settings

local:
	echo "Starting  local backend development server"
	poetry run .\backend\manage.py runserver
