from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Tarea
from .forms import TareaForm

# --- TAREAS ---
class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'tareas/list.html'
    context_object_name = 'tareas'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar') or ''
        return Tarea.objects.filter(usuario=self.request.user, titulo__icontains=buscar)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = Tarea.objects.filter(usuario=self.request.user, completo=False).count()
        return context

class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    template_name = 'tareas/detalle.html'

class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/form.html'
    success_url = reverse_lazy('tareas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/form.html'
    success_url = reverse_lazy('tareas')

class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = 'tareas/delete_confirm.html'
    success_url = reverse_lazy('tareas')

# --- CUENTAS ---
class Logeo(LoginView):
    template_name = 'cuenta/login.html'
    redirect_authenticated_user = True

class PaginaRegistro(CreateView):
    form_class = UserCreationForm
    template_name = 'cuenta/registro.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Cuenta creada. Puedes iniciar sesión.")
        return super().form_valid(form)