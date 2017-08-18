from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = [

	# Admin URL
    url(r'^admin/', admin.site.urls),

    # Home page
    url(r'^', include('home.urls', namespace='home'), name='home'),
    


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
