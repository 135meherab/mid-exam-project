from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from car.models import Car
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UpdateUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class register(CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login_page')
    def form_valid(self, form):
        messages.success(self.request, 'Account has been registered successfully. login with your username and password')
        return super().form_valid(form)

class login(LoginView):
    template_name = 'login.html'
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('home_page')
    
    
@login_required(login_url='login_page')
def profile(request):
    data = request.user
    cars = Car.objects.filter(buyer=request.user)
    return render(request, 'profile.html',{'data':data, 'cars':cars})


class edit_profile(LoginRequiredMixin,UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'edit_profile.html'
    pk_url_kwarg = 'id'	
    success_url = reverse_lazy('home_page')