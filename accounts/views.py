from .forms import RamenUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView


class SignUpView(CreateView):
    form_class = RamenUserCreationForm 
    success_url = reverse_lazy('accounts:login')  
    template_name = 'accounts/signup.html'      


class Home(TemplateView):
    template_name = 'home.html'


