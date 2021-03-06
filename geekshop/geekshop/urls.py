from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mainapp.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('basket/', include('basket.urls', namespace='basket')),
    path('admins/', include('admins.urls', namespace='admins')),
    path('', include('social_django.urls', namespace='social')),
    path('orders/',include('ordersapp.urls', namespace='orders'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
