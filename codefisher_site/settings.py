import os
BASE_DIR = os.path.realpath(os.path.dirname(__file__))

INTERNAL_IPS = (
    '127.0.0.1',
)

ADMINS = (
    ('Michael Buckley', 'support@codefisher.org'),
)

MANAGERS = ADMINS

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

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, '..', 'templates'),
)

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
    'djangopress.donate',
    'paypal.standard',
    'paypal.standard.ipn',
    'djangopress.contact',
    'djangopress.iptools',
    # other apps
    'tinymce',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)


PAYPAL_RECEIVER_EMAIL = "paypal@codefisher.org"
PAYPAL_TEST = False

KEEP_LOGGED_DURATION = 30*24*60*60 # about one month

X_FRAME_OPTIONS = 'DENY'

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

try:
    from mozbutton_sdk.config.settings import config

    MOZ_APP_NAMES = dict((ext_id, name) for name, ext_id, _, _ in
        sum(config.get("applications_data").values(), ()))
except ImportError:
    print("Could not import mozbutton_sdk")

# the default icons to use for the link buttons
DEFAULT_LINK_ICONS = "/home/michael/WebSites/dev/codefisher/www/static/images/link-icons"

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
    'plugins': "table code image link",
    'tools': "inserttable",

}
TINYMCE_JS_URL = "//tinymce.cachefly.net/4.2/tinymce.min.js"
