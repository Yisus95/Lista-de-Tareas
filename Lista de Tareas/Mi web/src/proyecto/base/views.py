from urllib import request, response

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView)
from django.views.generic.list import ListView

from .models import Tarea


class Logeo(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tareas")


class PaginaRegistro(FormView):
    template_name = "base/registro.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("tareas")

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
            messages.success(self.request, "Usuario creado correctamente")
        return super(PaginaRegistro, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("tareas")
        return super(PaginaRegistro, self).get(*args, **kwargs)


class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = "tareas"

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = context["tareas"].filter(completo=False).count()

        valor_buscado = self.request.GET.get("buscar") or ""
        if valor_buscado:
            context["tareas"] = context["tareas"].filter(
                titulo__icontains=valor_buscado
            )
        context["valor_buscado"] = valor_buscado
        return context


class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = "tarea"
    template_name = "base/tarea.html"


class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = ["titulo", "descripcion", "completo"]
    success_url = reverse_lazy("tareas")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "¡Tarea creada correctamente!")
        return response


class EditarTarea(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Tarea
    fields = ["titulo", "descripcion", "completo"]
    success_url = reverse_lazy("tareas")
    success_message = "¡Tarea actualizada correctamente!"

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)

    # si prefieres, puedes mantener form_valid:
    def form_valid(self, form):
        response = super().form_valid(form)
        # SuccessMessageMixin ya añade el mensaje; esta línea sería redundante
        # messages.success(self.request, "¡Tarea actualizada correctamente!")
        return response


class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = "tarea"
    template_name = "base/tarea_confirm_delete.html"
    success_url = reverse_lazy("tareas")

    def get_queryset(self):
        # solo las tareas del usuario
        return Tarea.objects.filter(usuario=self.request.user)

    def post(self, request, *args, **kwargs):
        # use post() para asegurarnos de interceptar el submit del form
        obj = self.get_object()
        print(
            f"DEBUG: EliminarTarea.POST called for pk={obj.pk} titulo='{obj.titulo}' user={request.user}"
        )
        # ejecutar la eliminación y captar la respuesta
        response = super().post(request, *args, **kwargs)
        # añadir mensaje justo después
        messages.success(request, f"¡Tarea «{obj.titulo}» eliminada correctamente!")
        print("DEBUG: mensaje añadido y response prepared")
        return response
