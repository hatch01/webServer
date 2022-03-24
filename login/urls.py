from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path("", csrf_exempt(views.base), name="base"),
    path("user_login/", csrf_exempt(views.user_login), name="user_login"),
  path("status", views.statut),
  path("status_modif/", csrf_exempt(views.status_modif)),

]