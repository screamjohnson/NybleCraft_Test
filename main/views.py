from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from main.models import MyUser
from django.core.signing import BadSignature
from .forms import RegisterUserForm
from .utilities import signer, send_activation_notification


def index(request):
    template = 'index.html'
    response = render(request, template)
    return render(request, 'index.html')


class UserLoginView(LoginView):
    template_name = "auth/login_form.html"
    success_url = 'auth/user_profile.html'


def profile(request):
    return render(request, 'auth/user_profile.html')


class RegisterUserView(CreateView):
    model = MyUser
    template_name = 'auth/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')

    # def form_valid(self, form):
    #     response = super(RegisterUserView, self).form_valid(form)
    #     send_activation_notification(user=self.object)
    #     return response


class RegisterDoneView(TemplateView):
    template_name = 'auth/register_done.html'


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'auth/bad_signature.html')
    user = get_object_or_404(MyUser, username=username)
    if user.is_activated:
        template = 'auth/user_activated.html'
    else:
        template = 'auth/user_activated_done.html'
        user.is_activated = True
        user.is_active = True
        user.save()
    return render(request, template)
