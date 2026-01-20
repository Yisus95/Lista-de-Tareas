from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
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
        response = super().form_valid(form)
        # Mensaje flash al crear
        messages.success(self.request, "Tarea creada correctamente.")
        return response

class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/form.html'
    success_url = reverse_lazy('tareas')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Mensaje flash al editar
        messages.success(self.request, "Tarea actualizada correctamente.")
        return response

class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = 'tareas/delete_confirm.html'
    success_url = reverse_lazy('tareas')

    def post(self, request, *args, **kwargs):
        # Se ejecuta al confirmar la eliminación (POST desde el formulario)
        self.object = self.get_object()
        # Mensaje flash limpio (sin debug)
        messages.success(request, f"Tarea «{self.object.titulo}» eliminada correctamente.")
        return super().post(request, *args, **kwargs)

    # mantenemos delete como fallback (llamado por super().post())
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

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