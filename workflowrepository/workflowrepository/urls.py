"""workflowrepository URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from data import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^workflow_list/(?P<category_slug>[-\w]+)/$', views.workflow_list, name='workflow_list_by_category'),
    url(r'^workflow_detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.workflow_detail, name='workflow_detail'),
    url(r'^admin/', admin.site.urls),
]
urlpatterns += static ( settings.STATIC_URL, \
                        document_root=settings.STATIC_ROOT)
