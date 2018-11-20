from django.conf.urls import url
from upload import views

urlpatterns = [
	url(r'^add_workflow/$', upload.add_workflow, name='add_workflow'),
]
