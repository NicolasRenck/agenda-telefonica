from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Agenda
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView


class ListaContatos(LoginRequiredMixin, ListView):
    model = Agenda
    context_object_name = 'agenda'
    template_name = 'pastaApp/lista.html'
    
    def get_queryset(self):
        return Agenda.objects.filter(usuario=self.request.user)


class AdicionarContato(LoginRequiredMixin, CreateView): 
    model = Agenda 
    fields = ['contato', 'numero'] 
    success_url = reverse_lazy('agenda') 
    template_name = 'pastaApp/add_contato.html'
    

    def form_valid(self, form): 
        form.instance.usuario = self.request.user 
        return super().form_valid(form)


class EditarContato(LoginRequiredMixin, UpdateView): 
    model = Agenda 
    fields = ['contato', 'numero'] 
    success_url = reverse_lazy('agenda') 
    template_name = 'pastaApp/edit_contato.html'  


class DeletarContato(LoginRequiredMixin, DeleteView):
    model = Agenda 
    context_object_name = 'agenda' 
    success_url = reverse_lazy('agenda') 
    template_name = 'pastaApp/contato_confirm_delete.html' 


class Registro(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')


