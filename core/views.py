from django.shortcuts import render, redirect
from django.views.generic import TemplateView,CreateView,View,ListView,UpdateView,DeleteView
from .models import Agenda, Local
from .forms import AgendaForm
class Index(View):
     def get(self, request):
          local = Local.objects.all()
          form = AgendaForm
          return render(request, 'index.html',{'local':local, 'form':form})
     
     def post(self, request):
          form = AgendaForm(request.POST)
          if form.is_valid():
               agendamento = form.save()
               agendamento.send_email()
               return redirect('index')
          else:
               form = AgendaForm()
          context = {
               'form':form
          }
          return render(request,'index.html',context=context)

