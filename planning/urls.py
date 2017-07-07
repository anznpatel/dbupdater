from django.conf.urls import url, include
from .views import update, show_version

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'update/$', update, name='planning_update'),
    url(r'version/$', show_version, name='show_version'),
]
