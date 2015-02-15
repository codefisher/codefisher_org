from django.conf.urls import patterns, include
from django.conf import settings
from flash_cards import urls as flash_cards_urls

from django.contrib import admin

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^flash_cards/', include(flash_cards_urls)),
)

# if debug is enabled use the static server for media
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)