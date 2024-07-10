import secrets
import random

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, PasswordResetForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{token}'
        send_mail(
            subject='Подтверждение почты',
            message=f'Перейдите по ссылке для подтверждения почты: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


def password_res(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = get_object_or_404(User, email=email)
        new_password = ''.join([str(random.randint(0, 9)) for i in range(12)])
        send_mail(
            subject='Вы сменили пароль',
            message=f'Ваш новый пароль: {new_password}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        user.set_password(new_password)
        user.save()
        return redirect('users:login')
    return render(request, 'users/reset_password.html')


class PasswordResetView(FormView):
    template_name = 'password_reset.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('users:login')