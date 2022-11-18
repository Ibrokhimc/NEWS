from .views import SignUpView
from django.urls import path

urlpatterns = [
    path(
        'accounts/', SignUpView.as_view(), name='signup'
    )
]