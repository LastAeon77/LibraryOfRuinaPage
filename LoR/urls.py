from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "lor"
urlpatterns = [
    path("", views.HomePage, name="Home"),
    path("card/", views.CardHomeView, name="CardHome"),
    path("office/", views.OfficeHomePage, name="OfficeHome"),
    path("office/<slug:slug>/", views.OfficeView.as_view(), name="Office"),
    path("rank/<slug:slug>/", views.RankView.as_view(), name="Rank"),
    path("card/<slug:slug>/", views.CardDetailView, name="Card"),
    path("deck/add/", views.deck_maker_form, name="DeckAdd"),
    path("deck/<int:pk>", views.deckView, name="DeckAdd"),

] + staticfiles_urlpatterns()
