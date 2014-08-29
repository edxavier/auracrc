from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.context import RequestContext
from django.shortcuts import render_to_response,get_object_or_404

# Create your views here.
class Inicio(TemplateView):
    def get(self, request):
        return render_to_response('inicio.html', locals(),context_instance=RequestContext(request))
