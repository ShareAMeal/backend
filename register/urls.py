
from django.urls import path, include
from register import views as v
from django.conf.urls import url

urlpatterns = [
    url(r'^signup/$', v.signup, name='signup'),
    url(r'^connexion/$', v.connexion, name='connexion'),
    url(r'^deconnexion/$', v.deconnexion, name='deconnexion'),
    url(r'^creerasso/$', v.creerasso, name='creerasso'),
    url(r'^afficheasso/$', v.afficheasso, name='afficheasso'),
    url(r'^creerevent/$', v.creerevent, name='creerevent'),
    url(r'^afficherevent/$', v.afficherevent, name='afficherevent'),
    url(r'^modifevent/(?P<event_id>[0-9]+)/$', v.modifevent, name='modifevent'),
    url(r'^$', v.index, name='index'),
]
