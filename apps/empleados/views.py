from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from apps.empleados.models import Empleado,Direccion
from apps.empleados.forms import EmpleadoForm,DireccionForm
# Create your views here.

class EmpleadosList(ListView):
    model = Empleado
    second_model = Direccion

    def get_queryset(self):
        queryset = self.model.objects.filter(activo=1).order_by('id')
        return queryset

class EmpleadosCreate(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    second_form_class = DireccionForm
    success_url = reverse_lazy('empleados:empleados_list')

    def get_context_data(self, **kwargs):
        context = super(EmpleadosCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            usuario = form.save(commit=False)
            #direccion = form2.save(commit=False)
            usuario.direccion = form2.save()
            usuario.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
              self.get_context_data(form=form, form2=form2))

class EmpleadosUpdate(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    second_form_class = DireccionForm
    success_url = reverse_lazy('empleados:empleados_list')

    def get_context_data(self, **kwargs):
        context = super(EmpleadosUpdate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            id_direccion=kwargs['form'].initial.get('direccion',0)
            try:
                direccion = Direccion.objects.get(id=id_direccion)
            except Direccion.DoesNotExist:
                pass
            form2 = self.second_form_class(instance=direccion)
            context['form2'] = form2
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_empleado = kwargs['pk']
        empleado = self.model.objects.get(id=id_empleado)
        form = self.form_class(request.POST,instance=empleado)
        id_direccion = self.request.POST.get('direccion')
        direccion = Direccion.objects.get(id=id_direccion)
        form2 = self.second_form_class(request.POST,instance=direccion)
        if form.is_valid() and form2.is_valid():
            form.save(commit=False)
            form2.save(commit=False)
            #usuario.direccion = form2.save()
            #usuario.save()
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else    :
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('empleados:empleados_list')


class EmpleadosDelete(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados:empleados_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo=0
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())