from django.conf.urls import url
from pages_service.views import *

urlpatterns = [
	url(r'^about/', aboutPage),

	# That page is called if not a single previous rule matches
	url(r'', startPage),
]

