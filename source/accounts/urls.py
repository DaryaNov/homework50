from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import RegisterView,RegisterActivateView,UserDetailView,UserPasswordChangeView,UserChangeView
app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='create'),

    path('activate/<uuid:token>/', RegisterActivateView.as_view(), name='activate'),
    path('<int:pk>/', UserDetailView.as_view(), name='view'),
    path('<int:pk>/update/', UserChangeView.as_view(), name='update'),
    path('<int:pk>/password-change/', UserPasswordChangeView.as_view(), name='password_update')
]