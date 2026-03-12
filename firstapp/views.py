from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from .utils import get_daily_code

today_str = get_daily_code()

@xframe_options_exempt
def home(request, today_str):
    return render(request, "home.html")
@xframe_options_exempt
def sandpainting(request, today_str):
    return render(request, "sandpainting.html")
@xframe_options_exempt
def cookie(request, today_str):
    return render(request, "cookie.html")
@xframe_options_exempt
def burrito(request, today_str):
    return render(request, "burrito.html")
@xframe_options_exempt
def web(request, today_str):
    return render(request, "web.html")
@xframe_options_exempt
def dash(request, today_str):
    return render(request, "dash.html")
@xframe_options_exempt
def test(request, today_str):
    return render(request, "test.html")
@xframe_options_exempt
def orders(request):
    return render(request, "orders.html")
@xframe_options_exempt
def minecraft(request, today_str):
    return render(request, "minecraft.html")
@xframe_options_exempt
def RetroBowl(request, today_str):
    return render(request, "Retro Bowl.html")
@xframe_options_exempt
def ships3d(request, today_str):
    return render(request, "ships3d.html")
@xframe_options_exempt
def code(request):
    return render(request, "code.html")