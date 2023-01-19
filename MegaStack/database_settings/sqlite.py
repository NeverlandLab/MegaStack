from MegaStack.settings import BASE_DIR
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, os.environ.get('DATABASE_NAME', 'db') + '.sqlite3'),
    }
}
