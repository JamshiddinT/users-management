from django.urls import path

from .views import SignUpView, HomePageView, UserActionsView, CustomLoginView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('user_actions/', UserActionsView.as_view(), name='user_actions'),
]
