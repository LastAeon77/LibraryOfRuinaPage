from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "LoR"
urlpatterns = [
    path("", views.HomePage, name="Home"),
    path("Card/", views.CardHomeView, name="CardHome"),
    path("Office/", views.OfficeHomePage, name="OfficeHome"),
    path("Office/<slug:slug>/", views.OfficeView.as_view(), name="Office"),
    path("Rank/<slug:slug>/", views.RankView.as_view(), name="Rank"),
    path("Card/<slug:slug>/", views.CardDetailView, name="Card"),
    path("Deck/add/", views.deck_maker_form, name="DeckAdd"),
] + staticfiles_urlpatterns()
