from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
@xframe_options_exempt
def home(request):
    return render(request, "home.html")
@xframe_options_exempt
def sandpainting(request):
    return render(request, "sandpainting.html")
@xframe_options_exempt
def cookie(request):
    return render(request, "cookie.html")
@xframe_options_exempt
def burrito(request):
    return render(request, "burrito.html")
@xframe_options_exempt
def web(request):
    return render(request, "web.html")
@xframe_options_exempt
def dash(request):
    return render(request, "dash.html")
@xframe_options_exempt
def test(request):
    return render(request, "test.html")
@xframe_options_exempt
def orders(request):
    return render(request, "orders.html")