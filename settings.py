# SETTINGS.PY

SECRET_KEY = "8912IOB8DHD89sbhui923uioh890dvH89H899GH78h89weh89n89h89sdf"

DATABASES = {
        'default': {
                #fill out if not using sqlite
                'ENGINE' : 'django.db.backends.sqlite3',
                'NAME': 'sqlite.db',
                'USER' : '',
                'PASSWORD': '',
                'HOST': '',
                'PORT': '',
            }
    }

INSTALLED_APPS = (
    'ormApp',
    )
