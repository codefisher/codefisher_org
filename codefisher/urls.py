from django.conf.urls import url, include
from django.conf import settings
from djangopress.forum import urls as forum_urls
from djangopress.accounts import urls as accounts_urls
from djangopress.blog import urls as blog_urls
from djangopress.pages import urls as pages_urls
from djangopress.files import urls as files_urls
from djangopress.gallery import urls as gallery_urls
from paypal.standard.ipn import urls as paypal_urls
from djangopress.donate import urls as donate_urls
from djangopress.contact import urls as contact_urls
from djangopress.iptools import urls as iptools_urls
from codefisher_apps.downloads import urls as download_urls
from codefisher_apps.svn_xslt import urls as svn_urls
from codefisher_apps.favicon_getter import urls as favicon_getter_urls
from codefisher_apps.pastelsvg import urls as pastelsvg_urls

from django.http import HttpResponsePermanentRedirect

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

admin.site.site_header = 'Codefisher Admin'

def redirect(request, url):
    return HttpResponsePermanentRedirect('/' + url)

# django databrowse application
#from django.contrib import databrowse
#from django.contrib.auth.decorators import login_required

urlpatterns = [
    # the blog system
    url(r'^(?P<blog_slug>[\w\-]+)/blog/', include(blog_urls)),
    url(r'^news/', include(blog_urls), {"blog_slug": "news"}),
    
    # the forum system
    url(r'^(?P<forums_slug>[\w\-]+)/forum/', include(forum_urls)),
    url(r'^forum/', include(forum_urls), {"forums_slug": "codefisher"}),
    
    # the user accounts system
    url(r'^accounts/', include(accounts_urls)),

    # the cms pages editing tools etc/
    url(r'^pages/', include(pages_urls)),

    url(r'^gallery/', include(gallery_urls)),
    url(r'^files/', include(files_urls)),
    url(r'^paypal/', include(paypal_urls)),
    url(r'^donate/', include(donate_urls)),
    url(r'^email/', include(contact_urls)),
    url(r'^iptools/', include(iptools_urls)),
    url(r'^(?P<url>.*/)[a-z_-]+\.php$', redirect),

    url(r'^xslt_svn/', include(svn_urls)),
    url(r'^ico/', include(favicon_getter_urls)),
    url(r'^pastel-svg/', include(pastelsvg_urls)),
    # the Toolbar Buttons section of the site (custom maker etc.)
    url(r'^toolbar_button/', include('tbutton_web.tbutton.urls')),
    url(r'^toolbar_button/', include('tbutton_web.tbutton_maker.urls')),
    url(r'^toolbar_button/', include('tbutton_web.lbutton.urls')),
]

try:
    if 'haystack' in settings.INSTALLED_APPS:
        from djangopress.core.search import ModelSetSearchForm, ModelSetSearchView, search_view_factory
        urlpatterns += [
            # the haystack search
            url(r'^search/', search_view_factory(
                    view_class=ModelSetSearchView,
                    form_class=ModelSetSearchForm,
                    results_per_page=10,
                    models=["pages.page", "blog.entry"],
                ), name='haystack-search'),
        ]
except ImportError:
    pass

try:
    import tinymce
    urlpatterns += [
        url(r'^tinymce/', include('tinymce.urls')),
    ]
except ImportError:
    pass

from djangopress.sitemap import sitemap_patterns
urlpatterns += sitemap_patterns

try:
    from .local_urls import urlpatterns as locale_urls
    urlpatterns = locale_urls + urlpatterns
except ImportError:
    pass

from codefisher_apps.downloads.urls import urlpatterns as download_urls
urlpatterns += download_urls

from djangopress.core.format.models import autodiscover as format_autodiscover
format_autodiscover()

from djangopress.theme.models import autodiscover as theme_autodiscover
theme_autodiscover()