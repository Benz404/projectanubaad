from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("/<int:my_id>",views.post,name="post"),
]