from django.shortcuts import render, redirect
from django.views.generic import TemplateView,CreateView,View,ListView,UpdateView,DeleteView
from django.contrib import messages

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
               
               messages.success(request, 'Seu Agendamento foi marcado, verifique seu E-mail')
               agendamento = form.save()
               agendamento.send_email()
          
               return redirect('index')
          else:
               messages.error(request, 'Erro no Agendamento. Por favor, verifique os dados.')
               form = AgendaForm()
          context = {
               'form':form
          }
          return render(request,'index.html',context=context)

