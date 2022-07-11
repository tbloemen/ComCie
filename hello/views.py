from django.utils.timezone import datetime
from django.shortcuts import render
from django.http import HttpResponse
import re

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = f"Hello there, {clean_name}. It's {formatted_now}."
    return HttpResponse(content)