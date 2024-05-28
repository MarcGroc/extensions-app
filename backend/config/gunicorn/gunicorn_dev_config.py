wsgi_app = "config.wsgi:application"
loglevel = "debug"
workers = 2
worker_class = "gevent"
bind = "0.0.0.0:8000"
reload = True
timeout = 60
