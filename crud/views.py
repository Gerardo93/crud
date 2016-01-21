from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from crud.forms import RegistrarForm

def home(request):
    return render_to_response('home.html')

def Registrar(request):
    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]


            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegistrarForm()

    data = {
        'form': form,
    }
    return render_to_response('registrar_usuario.html', data, context_instance=RequestContext(request))