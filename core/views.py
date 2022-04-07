from django.views.generic import FormView, TemplateView

from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContatoForm

class IndexView(FormView):
    template_name = 'index.html'
    
    form_class = ContatoForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
    
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, "E-mail enviado com sucesso")
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "Erro ao enviar e-mail")
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
    
    
class PortfolioDetails1View(TemplateView):
    template_name = 'portfolio-details1.html' #ano 2017

class PortfolioDetails2View(TemplateView):
    template_name = 'portfolio-details2.html' #ano 2018

class PortfolioDetails3View(TemplateView):
    template_name = 'portfolio-details3.html' #ano 2019


    