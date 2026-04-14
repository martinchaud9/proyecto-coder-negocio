from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen'] # Los campos que queremos que llenen
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user # Asigna automáticamente al autor logueado
        return super().form_valid(form)

class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    
class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    
class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "blog/post_form.html" # Reutilizamos el mismo formulario de crear
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    success_url = reverse_lazy('post_list')

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy('post_list')