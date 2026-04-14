from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Message
from django.contrib.auth.models import User

# Bandeja de entrada
class InboxView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "messaging/inbox.html"
    context_object_name = "messages"

    def get_queryset(self):
        # Solo mostramos los mensajes donde el usuario actual es el RECEPTOR
        return Message.objects.filter(receiver=self.request.user).order_by('-timestamp')

# Enviar mensaje
class SendMessageView(LoginRequiredMixin, CreateView):
    model = Message
    template_name = "messaging/send_message.html"
    fields = ['receiver', 'content']
    success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        form.instance.sender = self.request.user # El emisor es el usuario logueado
        return super().form_valid(form)