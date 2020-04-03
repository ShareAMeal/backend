
from django.urls import path, include
from register import views as v
from django.conf.urls import url

urlpatterns = [
    url(r'^signup/$', v.signup, name='signup'),
    url(r'^ok/$', v.ok, name='ok'),
    url(r'^connexion/$', v.connexion, name='connexion'),
    url(r'^deconnexion/$', v.deconnexion, name='deconnexion'),
    url(r'^creerasso/$', v.creerasso, name='creerasso'),
]
