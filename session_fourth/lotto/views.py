from django.shortcuts import render
import random

def home(request):
    return render(request, 'lotto/home.html')

def result(request):
    #num = random.sample(range(1, 47), 6)
    #return render(request, 'lotto/result.html', {'num' : num})
    
    num = random.sample(range(1, 47), 6)

    list = ('사과', '귤', '포도', '배', '감', '복숭아')
    fruits = random.sample(list, 2)

    return render(request, 'lotto/result.html', {'num' : num, 'fruits' : fruits})