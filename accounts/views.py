from django.views.generic import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomChangeForm
from django.urls import reverse_lazy
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')