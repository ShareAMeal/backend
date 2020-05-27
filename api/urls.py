from rest_framework import routers

from . import views

router = routers.DefaultRouter()
# router.register(r'asso', views.AssoViewset)
# router.register(r'event', views.EventViewset)

urlpatterns = router.urls + [

]