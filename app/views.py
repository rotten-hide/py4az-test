from django.shortcuts import render

# Create your views here.
def template(request):
    return render(request, 'app/template.html')

def index(request):
    context = {'test': 'test'}
    return render(request, 'app/index.html')