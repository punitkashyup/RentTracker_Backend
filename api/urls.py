from django.urls import path
from .views import SendPasswordResetEmailView,UserAvatarUpload, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView
from .views import countViews, rentViews

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path("api/user-avatar/", UserAvatarUpload.as_view(), name="rest_user_avatar_upload"),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('count/', countViews.as_view()),
    path('rent/', rentViews.as_view()),
    path('rent/<int:id>', rentViews.as_view()),

]