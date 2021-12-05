from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# app_name allows for easier calling of url in html
app_name = "lor"
# these are the url patterns for each page of the website
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
    path("api/deck/<int:pk>", views.deckSerail.as_view(), name="DeckAPIView"),
    path("api/card/", views.CardListView.as_view(), name="CardAPIView"),
    path("api/abno/", views.AbnoViewSet.as_view(), name="AbnoAPIView"),
    path("abno/", views.AbnoList, name="AbnoHome"),
    path("abno/<int:pk>", views.AbnoView.as_view(), name="Abno"),
    path("api/effects", views.EffectListView.as_view(), name="Effects"),
    path("api/deck/",views.DeckListView.as_view(),name="DeckAllView"),
    path("api/deckpure/",views.PureDeckListView.as_view(),name="PureDeckAllView"),
] + staticfiles_urlpatterns()
