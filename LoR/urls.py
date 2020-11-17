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
    path("deck/<int:pk>", views.deckView, name="Deck"),
    path("deck", views.deckHomeView, name="DeckHome"),
    path("character/<slug:slug>", views.CharView.as_view(), name="Char"),
    path("character", views.CharacterList, name="CharHome"),
    path("page/<slug:slug>", views.PageView.as_view(), name="Page"),
    path("page", views.PageList, name="PageHome"),
    path("guide/<int:pk>", views.GuideView, name="Guide"),
    path("guide", views.guideHomeView.as_view(), name="GuideHome"),
    path("guide/add", views.guide_maker_form, name="GuideAdd"),


] + staticfiles_urlpatterns()
