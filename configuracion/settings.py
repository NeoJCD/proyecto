from pathlib import Path
from datetime import timedelta

# 1. RUTAS Y CLAVES
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-clave-secreta-para-neomar'
DEBUG = True
ALLOWED_HOSTS = ['*']

# 2. APLICACIONES INSTALADAS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # TUS APPS Y LIBRERIAS:
    'rest_framework',
    'rest_framework_simplejwt',
    'tareas',
    'petrolera',
]

# 3. MIDDLEWARE (¡Esto era lo que faltaba!)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 4. CONFIGURACIÓN DE URLS Y SERVIDOR
ROOT_URLCONF = 'configuracion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Conecta tu carpeta templates en la raíz
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

WSGI_APPLICATION = 'configuracion.wsgi.application'

# 5. BASE DE DATOS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 6. VALIDACIÓN DE CONTRASEÑAS
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

# 7. IDIOMA Y ZONA HORARIA
LANGUAGE_CODE = 'es-ve'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 8. ARCHIVOS ESTÁTICOS
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 9. CONFIGURACIÓN DE SEGURIDAD JWT (Tu personalización)
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    # ¡IMPORTANTE! Usamos tu serializer personalizado aquí
    'TOKEN_OBTAIN_SERIALIZER': 'petrolera.customtoken.CustomTokenObtainPairSerializer',
}

# 10. CONFIGURACIÓN DE DRF (API REST)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    # Límites de velocidad (Throttling)
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.ScopedRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'tecnicos': '10/minute',
        'administrativos': '5/minute',
        'seguridad': '100/minute',
    }
}