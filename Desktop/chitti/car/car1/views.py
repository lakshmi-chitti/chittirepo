from django.shortcuts import render

# Creadefte your views here.

def carshouse(request):
    values={"name":"lakshmi","age":20}
    return render(request,'car1/cars.html',values)
