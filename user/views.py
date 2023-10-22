from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView


from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm


class HomePageView(ListView):
    model = CustomUser
    ordering = ['-id']
    template_name = 'home.html'


class UserActionsView(LoginRequiredMixin, View):
    template_name = 'home.html'

    def post(self, request, *args, **kwargs):
        
        if request.user.status == 'BLOCKED':
            return redirect('login')
        
        print(request.user.status)
        action = request.POST.get('action')
        user_ids = request.POST.get('user_ids').split(',')
        print(user_ids)
        profiles = CustomUser.objects.filter(id__in=user_ids).exclude(is_superuser=True)

        if action == 'block':
            profiles.exclude(is_superuser=True).update(status='BLOCKED')
        elif action == 'unblock':
            profiles.exclude(is_superuser=True).update(status='ACTIVE')
        elif action == 'delete':
            profiles.exclude(is_superuser=True).delete()

        return redirect('home')
