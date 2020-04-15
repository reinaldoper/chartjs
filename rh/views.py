from django.contrib.auth.forms import UserCreationForm
from django.core.serializers import json
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
import json

from django.views.generic import TemplateView

from .models import Ganhos
from .forms import GanhosForm


class index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Ganhos.objects.all()
        return context


def cards(request):
    return render(request,'cards.html')


def buttons(request):
    if request.method == 'POST':
        form = GanhosForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = GanhosForm()
        return render(request, 'buttons.html', {'form': form})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
# Create your views here.
