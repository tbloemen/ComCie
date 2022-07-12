from email import message
from typing import *
from django.utils.timezone import datetime
from django.shortcuts import redirect, render
from comcie.forms import LogMessageForm
from django.views.generic import ListView
from comcie.models import LogMessage

# Create your views here.


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


def hello_there(request, name):
    return render(
        request,
        'comcie/hello_there.html',
        {
            'name': name,
            'date': datetime.now(),
        }
    )


def about(request):
    return render(request, "comcie/about.html")


def contact(request):
    return render(request, "comcie/contact.html")


def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(
            request,
            "comcie/log_message.html",
            {
                'form': form
            }
        )
