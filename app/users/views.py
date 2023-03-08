from django.views.generic import FormView, DetailView
from django.urls import reverse_lazy
from .forms import UserForm
from .models import User


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'



