from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'asso', views.AssoViewset, 'asso')
router.register(r'event', views.EventViewset, 'events')
router.register(r'myuser', views.TestAuthViewSet, 'myuser')

urlpatterns = router.urls + [

]