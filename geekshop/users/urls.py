from django.urls import path
from .views import LoginLoginView, LogoutView, RegisterListview, ProfileFormView

app_name = 'users'

urlpatterns = [

    path('login/', LoginLoginView.as_view(), name='login'),
    path('register/', RegisterListview.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileFormView.as_view(), name='profile'),
]
