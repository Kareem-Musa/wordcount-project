from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def count(request):
    fullText = request.GET['counts']
    words = fullText.split()
    return render(request,'count.html' , {'fullText':fullText , 'words':len(words)})

def about(request):
    return render(request,'about.html')
