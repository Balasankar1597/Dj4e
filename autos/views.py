from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from autos.models import Auto, Make


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Make.objects.all().count()
        al = Auto.objects.all()

        ctx = {'make_count': mc, 'auto_list': al}
        return render(request, 'autos/auto_list.html', ctx)



class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Make.objects.all()
        ctx = {'make_list': ml}
        return render(request, 'autos/make_list.html', ctx)


class MakeCreateView(LoginRequiredMixin,CreateView):

    template = "autos/make_form.html"
    success_url = reverse_lazy('autos:all')


    def get(self,request):
        return render(request,"autos/make_form.html")

    def post(self,request):
        data = request.POST['make']
        name = data
        make = Make()
        make.name = name
        make.save()

        return render(request,"autos/auto_list.html")




