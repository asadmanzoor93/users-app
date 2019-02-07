from django.urls import path
from users import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='user_signup'),
    path('login/', views.LoginUser.as_view(), name='user_login'),
    path('logout/', views.LogoutUser.as_view(), name='user_logout'),
    path('update_profile/', views.UpdateProfile.as_view(), name='user_profile'),
]
