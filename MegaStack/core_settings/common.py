import os

from MegaStack.core_settings.base_settings import DEBUG
from MegaStack.settings import BASE_DIR

SECRET_KEY = 'django-insecure-(-cl*#ehxkve)i27d2@*d&gj31+iv@zb%0&o^s#ga!$c#ri!ew'

ALLOWED_HOSTS = ["*"]
ROOT_URLCONF = 'MegaStack.urls'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_createsuperuserwithpassword',
    'corsheaders',
    'nested_inline',
    'smart_selects',
    'import_export',
    'rest_framework',
    'django_celery_results',
    'django_celery_beat',
    'drf_yasg',
    'apps.core',
    'apps.sample',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

if DEBUG:
    # Django-Debug-Tool-Bar 配置
    INTERNAL_IPS = [
        "127.0.0.1",
    ]

    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MegaStack.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

# 开发阶段放置项目自己的静态文件
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
]

# 执行collectstatic命令后会将项目中的静态文件收集到该目录下面来（所以不应该在该目录下面放置自己的一些静态文件，因为会覆盖掉）
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_ROOT = "media"
MEDIA_URL = "/media/"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

SERVER_LOGS_FILE = os.path.join(BASE_DIR, "logs", "server.log")
ERROR_LOGS_FILE = os.path.join(BASE_DIR, "logs", "error.log")
if not os.path.exists(os.path.join(BASE_DIR, "logs")):
    os.makedirs(os.path.join(BASE_DIR, "logs"))

STANDARD_LOG_FORMAT = (
    "[%(asctime)s][%(name)s.%(funcName)s():%(lineno)d] [%(levelname)s] %(message)s"
)
CONSOLE_LOG_FORMAT = (
    "[%(asctime)s][%(name)s.%(funcName)s():%(lineno)d] [%(levelname)s] %(message)s"
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": STANDARD_LOG_FORMAT},
        "console": {
            "format": CONSOLE_LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "file": {
            "format": CONSOLE_LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": SERVER_LOGS_FILE,
            "maxBytes": 1024 * 1024 * 100,  # 100 MB
            "backupCount": 5,  # 最多备份5个
            "formatter": "standard",
            "encoding": "utf-8",
        },
        "error": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": ERROR_LOGS_FILE,
            "maxBytes": 1024 * 1024 * 100,  # 100 MB
            "backupCount": 3,  # 最多备份3个
            "formatter": "standard",
            "encoding": "utf-8",
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
    },
    "loggers": {
        # default日志
        "": {
            "handlers": ["console", "error", "file"],
            "level": "INFO",
        },
        "django": {
            "handlers": ["console", "error", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "scripts": {
            "handlers": ["console", "error", "file"],
            "level": "INFO",
            "propagate": False,
        },
        # 数据库相关日志
        "django.db.backends": {
            "handlers": [],
            "propagate": True,
            "level": "INFO",
        },
    },
}
