# SETTINGS.PY
import os

SECRET_KEY = "mnkalsyuf8d9p3089hioyqwocmeau8902ikon24n2412oh4hjklashui010"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# change as needed based on environment
DATABASE_ENGINE = "django.db.backends.sqlite3"
DATABASE_NAME = os.path.join(BASE_DIR,"db.sqlite3")
