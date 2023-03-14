from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import FormView, DetailView
from django.urls import reverse_lazy
from .forms import NewUserForm
from django.contrib.auth.models import User


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = NewUserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



@login_required(login_url='login_user')
def user_profile(request):
    user = request.user
    #order = Order.objects.filter(customer=user)
    context = {'user': user}#, 'cart': Cart(request), 'order': order}
    return render(request, 'users/profile.html', context)

