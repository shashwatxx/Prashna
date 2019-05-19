from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from prashna import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prashna/', include('uttar.urls')),
    url('^$', RedirectView.as_view(url='prashna/')),
    url(r'^accounts/profile/$', RedirectView.as_view(url="/prashna/")),                
    url(r'^accounts/', include('registration.backends.default.urls')),                    
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

