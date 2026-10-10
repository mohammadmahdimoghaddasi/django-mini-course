from django.views.generic import ListView
from .models import Message

#def messageView(request):
 #   return render(request, 'index.html')
 
class MessageView(ListView):
    model = Message
    template_name = 'index.html'