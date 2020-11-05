from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "LoR"
urlpatterns = [
    path("", views.HomePage, name="Home"),
    #path("Card/", views.DetailView.as_view(), name="Card"),
    path("Office/", views.OfficeHomePage, name="OfficeHome"),
    path("Office/<slug:slug>/", views.OfficeView.as_view(), name="Office"),
    path("Rank/<slug:slug>/", views.RankView.as_view(), name="Rank"),
    path("Card/<int:pk>/", views.CardDetailView, name="Card"),
] + staticfiles_urlpatterns()
