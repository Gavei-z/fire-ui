from django.urls import path, include
from web.views import index, getinfo, getimg, saveres


urlpatterns = [
    path("", index, name="index"),
    path("getinfo/", getinfo, name="getinfo"),
    path("getimg/", getimg, name="getimg"),
    path("saveres/", saveres, name="saveres"),
]