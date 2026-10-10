from django.views.generic import TemplateView

#def messageView(request):
 #   return render(request, 'index.html')
 
class MessageView(TemplateView):
    template_name = 'index.html'