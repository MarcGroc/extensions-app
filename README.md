# Django/ Vue template

### Installation

#### Clone the repository
```bash
git clone https://github.com/sergey-morozov/django-vue-template.git
```
#### Create virtual environment
```bash
python3 -m venv /venv
source /venv/bin/activate
```

#### Install dependencies
``` bash
pip install -r /requirements/requirements.txt && pip install -r /requirements/dev-requirements.txt
```
#### Create env files
``` bash
touch .env/env.dev && touch .env/env.prod
```

#### Copy content from .env.example to .env.dev
``` bash
cp .env.example .env/dev
```
#### Replace default values in .env.dev
#### Change directory to backend
``` bash
cd django-vue-template/backend
```

#### Make migrations for users app
``` bash
python manage.py makemigrations users
```

#### Migrate to db
``` bash
python manage.py migrate
```
