from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.

class LandingView(View):
	def get(self, request):
		return render(request, 'landing.html')

class IndexView(View):
	def get(self, request):
		return render(request, 'index.html')
