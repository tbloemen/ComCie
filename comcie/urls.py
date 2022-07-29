from django.urls import path

from comcie import views
from comcie.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],
    context_object_name="message_list",
    template_name="comcie/home.html"
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
    path("musicians/", views.log_musician, name='musicians'),
    path("musicians/search_results", views.query_musicians,
         name="musician_search_results"),
    path("musicians/<name>", views.musician_menu, name='name_handler'),
]
