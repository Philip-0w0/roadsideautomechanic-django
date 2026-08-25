from django.contrib import admin
from django.urls import path, include, reverse
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'services', 'modifications', 'gallery', 'about', 'contact']

    def location(self, item):
        return reverse(item)


sitemaps = {'static': StaticViewSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('accounts/', include('accounts.urls')),
    path('booking/', include('bookings.urls')),
    path('', include('core.urls')),
    path('invoices/', include('invoices.urls')),
]