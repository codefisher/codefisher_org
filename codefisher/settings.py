import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)
djangopress = os.path.realpath(os.path.join(BASE_DIR, '..', 'djangopress'))
if djangopress not in sys.path:
    sys.path.append(djangopress)
mozbutton_sdk = os.path.realpath(os.path.join(BASE_DIR, '..', 'mozbutton_sdk'))
if mozbutton_sdk not in sys.path:
    sys.path.append(mozbutton_sdk)
codefisher_org = os.path.realpath(os.path.join(BASE_DIR, '..'))
if codefisher_org not in sys.path:
    sys.path.append(codefisher_org)
codefisher_apps = os.path.realpath(os.path.join(BASE_DIR, '..', 'codefisher_apps'))
if codefisher_apps not in sys.path:
    sys.path.append(codefisher_apps)

ADMINS = (
    ('Michael Buckley', 'support@codefisher.org'),
)
MANAGERS = ADMINS


from local_settings import *

MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'www', 'media')
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'www', 'static_files')
MEDIA_UPLOAD = MEDIA_ROOT

TBUTTON_CONFIG = (
    os.path.realpath(
        os.path.join(BASE_DIR, '..', 'toolbar_buttons/toolbar_button.json')),
    os.path.realpath(
        os.path.join(BASE_DIR, '..', 'toolbar_buttons/local.json')),
    os.path.realpath(os.path.join(BASE_DIR, '..', 'toolbar_buttons/web.json'))
)


from djangopress.settings_tinymce import TINYMCE_DEFAULT_CONFIG, TINYMCE_JS_URL
from djangopress.settings import ACCOUNTS_USER_LIMITS

INTERNAL_IPS = (
    '127.0.0.1',
)
ALLOWED_HOSTS = ["127.0.0.1", "codefisher.org"]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC' #None

USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

ROOT_URLCONF = 'codefisher_org.codefisher.urls'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.redirects',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    # codefisher
    'codefisher_org.codefisher_site',
    # djangopress
    'djangopress.core.format',
    'djangopress.blog',
    'djangopress.menus',
    'djangopress.core',
    'djangopress.accounts',
    'djangopress.theme',
    'djangopress.pages',
    'djangopress.forum',
    'djangopress.gallery',
    'djangopress.files',
    'djangopress.donate',
    'paypal.standard',
    'paypal.standard.ipn',
    'djangopress.contact',
    'djangopress.iptools',
    # other apps
    'tinymce',
)

try:
    INSTALLED_APPS += EXTRA_INSTALLED_APPS
except:
    pass

PAYPAL_RECEIVER_EMAIL = "paypal@codefisher.org"
PAYPAL_TEST = False

KEEP_LOGGED_DURATION = 30*24*60*60 # about one month

X_FRAME_OPTIONS = 'SAMEORIGIN'

ANONYMOUS_USER_GROUP = "Anonymous"
DEFAULT_USER_GROUP = "New Member"

# the icon sets to use for the buttons
#TBUTTON_ICONS = {
#    "pastel-svg": ("Pastel SVG", "../www/static/images/pastel-svg"),
#}

TBUTTON_ICONS_SIZES = [
    "standard", "large", "jumbo",
]
TBUTTON_ICON_SET_SIZES = {
    "pastel-svg": {
        "standard": ("16", "24"),
        "large": ("24", "32"),
        "jumbo": ("32", "48")
    },
}
TBUTTON_DEFAULT_ICONS = "pastel-svg"
#TBUTTON_TAGS_DIR = None

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '..', 'www', 'static'),
)

try:
    from mozbutton_sdk.config.settings import config
    MOZ_APP_NAMES = dict((ext_id, name) for name, ext_id, _, _ in
        sum(config.get("applications_data").values(), ()))
except ImportError:
    print("Could not import mozbutton_sdk")

# the default icons to use for the link buttons
DEFAULT_LINK_ICONS = os.path.realpath(os.path.join(BASE_DIR, '..', 'www/static/images/link-icons'))

GEOLITE2_DATABASE_FILE = os.path.realpath(os.path.join(BASE_DIR, '..', 'db/GeoLite2-City.mmdb'))

INSTALLED_APPS += (
    'tbutton_web.tbutton_maker',
    'tbutton_web.tbutton_votes',
    'tbutton_web.tbutton',
    'tbutton_web.lbutton',
    'codefisher_apps.downloads',
    'codefisher_apps.extension_downloads',
    'codefisher_apps.svn_xslt',
    'codefisher_apps.favicon_getter',
    'codefisher_apps.reverseproxy',
    'codefisher_apps.online_status',
    'codefisher_apps.site_crawler',
    'codefisher_apps.pastelsvg',
    'upvotes',
    'haystack',
    'captcha',
)

SITE_CRAWLER_DICT_LANG = "en"
SITE_CRAWLER_DICT_PWL = os.path.join(BASE_DIR, '..', 'wordlist.txt')
SITE_CRAWLER_REMOVE_IDS = ('footer', 'donations')


ACCOUNTS_USER_LIMITS = {
    "avatar": {
        "size": 50,
        "file_size": 1024*100,
        "max_upload_size": 200,
    },
    "attachments": {
        "file_size": 1024*500,
        "total": 1024*1024*5,
    },
    "signature": {
        "lines": 4,
        "length": 500,
        "images": True,
        "links": True,
    }
}

TINYMCE_DEFAULT_CONFIG = {
    'relative_urls': False,
    'plugins': "table code image link colorpicker textcolor wordcount",
    'tools': "inserttable",
    'toolbar': "undo redo | styleselect | bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | forecolor backcolor",
    'extended_valid_elements': 'script,events,gallery'
}
TINYMCE_JS_URL = "/static/js/tinymce/tinymce.min.js"

MIDDLEWARE_CLASSES = [
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'codefisher_apps.reverseproxy.middleware.ProxyMiddleware',
    'djangopress.pages.middleware.PagesMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'djangopress.accounts.middleware.TimezoneMiddleware',
    'djangopress.accounts.middleware.LastSeenMiddleware',
    'codefisher_apps.online_status.middleware.OnlineStatusMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
]

SMILIES_ICON_FOLDER = "/static/images/pastel-svg/16/"

if not DEBUG:
    # Django Secure
    SECURE_BROWSER_XSS_FILTER = True
    # SECURE_CONTENT_TYPE_NOSNIFF = True
    # SECURE_SSL_REDIRECT = True
    RECAPTCHA_USE_SSL = True
    MIDDLEWARE_CLASSES.insert(3, 'djangosecure.middleware.SecurityMiddleware')

    SESSION_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')