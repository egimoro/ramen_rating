from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View
from django.urls import reverse_lazy
from django.forms.models import model_to_dict
from .forms import RamenForm
from .models import Ramen

class RamenHome(LoginRequiredMixin, View):
    def get(self, request):
        form = RamenForm()
        return render(request, 'rating/ramen.html', {'form': form})

   




class RamenAdd(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        data = dict()
        if self.request.is_ajax and self.request.method == 'POST':
            form = RamenForm(self.request.POST)
            if form.is_valid():
                ramen = form.save()
                data['ramen'] = model_to_dict(ramen)
                return JsonResponse(data)
            else:
                return JsonResponse({'error': form.errors}, status=400)
        return JsonResponse({'error': ''}, status=400) 

    def form_valid(self, form):
        form.instance.rameuser = self.request.user
        return super(RamenAdd, self).form_valid(form)
            

    
        

class RamenList(View):
    def get(self, request):
        ratings = list(Ramen.objects.all().values())
        data = dict()
        data['rating_list'] = ratings
        return JsonResponse(data)
   
    
class RamenDetail(View):
    def get(self, request, id):
        rating = Ramen.objects.get(id=id)
        data = dict()
        data['rating'] = model_to_dict(rating)
        return JsonResponse(data)


class RamenUpdate(View):
    def post(self, request, id):
        data = dict()
        
        if request.is_ajax and request.method == 'POST':
            rating = Ramen.objects.get(id=id)
            form = RamenForm(instance=rating, data=request.POST)
            if form.is_valid():
                rating = form.save()
                data['rating'] = model_to_dict(rating)
                return JsonResponse(data)
            else:
                return JsonResponse({'error': form.errors}, status=400)
        return JsonResponse({'error': ''}, status=400)  


class RamenDelete(View):
    def post(self, request, id):
        data = dict()
        rating = Ramen.objects.get(id=id)
        if rating:
            rating.delete()
            data['message'] = 'Rating deleted!'
        else:
            data['message'] = 'Error!'
        
        return JsonResponse(data)