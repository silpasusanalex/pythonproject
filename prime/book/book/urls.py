"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from store.views import adminlogin_view,studentlogin_view,register_view
# from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', register_view),
     url(r'^student/$',studentlogin_view),
    #url(r'^login_processor/', log_p),
    #url(r'^login/',studentlogin_view),
    #url(r'^login/',adminlogin_view)
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

