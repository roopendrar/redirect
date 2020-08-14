from django.urls import path
from app9 import views
app_name="app9"


urlpatterns = [
    path('register/',views.register,name="register"),
    path("profile/",views.profile,name="profile"),
]
