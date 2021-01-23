from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import (
    Office,
    Rank,
    Card,
    Deck,
    RelDeck,
    Page,
    Character,
    Guide,
    RelGuide,
    AbnoCards,
    Effects
)
from .forms import DeckMakerForm, GuideMakerForm
from django.urls import reverse
import collections
from django.contrib.auth.decorators import login_required
from django.views import generic  # generic.DetailView and generic.ListView
from rest_framework import generics
from .serializers import (
    DeckSerializers,
    CardSerializers,
    RankSerializers,
    AbnoSerializers,
    EffectSerializers
)

# DetailView will fetch a certain row through its unique id in url
# ListView will fetch all rows of a Relation


# Simple Homepage
def HomePage(request):
    return render(request, "LoR/LoRHomePage.html")


# This is the homepage of offices, displays an Office id = pk
class OfficeView(generic.DetailView):
    model = Office
    template_name = "LoR/OfficeDetail.html"


# This is the homepage of Ranks, display a Rank id = pk
class RankView(generic.DetailView):
    model = Rank
    template_name = "LoR/RankDetail.html"


class rankSerial(generics.RetrieveAPIView):
    queryset = Rank.objects.all()
    serializer_class = RankSerializers


# This is the Office Homepage
def OfficeHomePage(request):
    # Gets all Office
    Offc = Office.objects.all()
    # This is an example of a "Raw" SQL performed through django's embedded SQL
    # Gets Rank id, Rank Name, number of Office in Rank, and the slug of Rank
    NumberOfOff = Office.objects.raw(
        """
SELECT O."Rank_id" AS id, R."Name", COUNT(*) AS "rank_num", R."slug"
FROM "LoR_office" AS O INNER JOIN "LoR_rank" AS R ON O."Rank_id" = R."id"
GROUP BY O."Rank_id", R."Name", R."slug"
ORDER BY O."Rank_id"
"""
    )

    context = {"Office": Offc, "Counting": NumberOfOff}
    return render(request, "LoR/OfficeHome.html", context)


# This is the view for a Card
def CardDetailView(request, slug):
    # Gets Card information, its Rank, its Office, its Rank Image Path, and its Office Image Path with corresponding slug
    pag = Card.objects.raw(
        f"""SELECT C.*, R."Name" AS "Rank", O."Name" AS "off",R."ImgPath" AS "RankImg", O."ImgPath" AS "OffImg"
FROM "LoR_office" AS O , "LoR_card" AS C,"LoR_rank" AS R
WHERE R."id" = O."Rank_id" AND O."id" = C."office_id" AND C."slug" = '{slug}'"""
    )
    context = {"card": pag[0]}
    return render(request, "LoR/CardDetail.html", context)


class cardSerial(generics.RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializers


# This is a view for the list of all the cards
def CardHomeView(request):
    # Gets all Card Object
    Cards = Card.objects.all()
    # Gets all Office id, Rank, Name, Number of Cards, Slug, and Image Path
    Offices = Card.objects.raw(
        """SELECT O."id",O."Rank_id",O."Name" AS "OfficeName",COUNT(*) AS "NumberOfCards", O."slug", O."ImgPath"
FROM ("LoR_office" AS O INNER JOIN "LoR_card" AS C ON O."id" = C."office_id")
GROUP BY O."id"
ORDER BY O."id"
"""
    )

    # Get all Rank Name, id, Number of Offices in Rank, slug, and image path.

    Ranks = Card.objects.raw(
        """SELECT R.id AS id,R."Name" AS RankName,COUNT(*) AS "NumberOfOffices", R."slug",R."ImgPath"
FROM ("LoR_office" AS O LEFT JOIN "LoR_rank" AS R ON O."Rank_id" = R."id")
GROUP BY R."id"
ORDER BY R."id"
            """
    )
    context = {"card": Cards, "office": Offices, "rank": Ranks}
    return render(request, "LoR/CardHome.html", context)


# This form allows user to make their own decks!
@login_required
def deck_maker_form(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            form = DeckMakerForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data["deck_name"]
                creator = request.user
                desc = form.cleaned_data["deck_description"]
                recc_floor = form.cleaned_data["Reccomended_Floor"]
                recc_page = form.cleaned_data["Reccomended_Page"]
                recc_rank = form.cleaned_data["Reccomended_Rank"]
                card1 = form.cleaned_data["card_1"]
                card2 = form.cleaned_data["card_2"]
                card3 = form.cleaned_data["card_3"]
                card4 = form.cleaned_data["card_4"]
                card5 = form.cleaned_data["card_5"]
                card6 = form.cleaned_data["card_6"]
                card7 = form.cleaned_data["card_7"]
                card8 = form.cleaned_data["card_8"]
                card9 = form.cleaned_data["card_9"]
                show = form.cleaned_data["show"]
                list_of_card = [
                    card1,
                    card2,
                    card3,
                    card4,
                    card5,
                    card6,
                    card7,
                    card8,
                    card9,
                ]
                y = collections.Counter(list_of_card)
                q = Deck(
                    name=name,
                    creator=creator,
                    description=desc,
                    Recc_Floor=recc_floor,
                    Recc_Page=recc_page,
                    Recc_Rank=recc_rank,
                    show=show,
                )
                q.save()
                eff_1 = form.cleaned_data["eff_1"]
                eff_2 = form.cleaned_data["eff_2"]
                eff_3 = form.cleaned_data["eff_3"]
                eff_4 = form.cleaned_data["eff_4"]

                eff_list = [eff_1, eff_2, eff_3, eff_4]
                eff_list = list(dict.fromkeys(eff_list))
                for effs in eff_list:
                    if effs is not None:
                        q.effect.add(effs)
                for cards in y:
                    q.cards.add(cards, through_defaults={"card_count": y[cards]})
                q.save()  # commits and saves data into database
                return HttpResponseRedirect(reverse("lor:Deck", args=(q.id,)))

        else:
            form = DeckMakerForm()
        context = {"form": form}
        return render(request, "LoR/deckMakingForm.html", context)
    else:
        return HttpResponseRedirect(reverse("register"))


# this is the view for user to create a guide
@login_required
def guide_maker_form(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = GuideMakerForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data["guide_name"]
                creator = request.user
                desc = form.cleaned_data["guide_description"]
                recc_floor = form.cleaned_data["floor"]
                deck1 = form.cleaned_data["deck_1"]
                deck2 = form.cleaned_data["deck_2"]
                deck3 = form.cleaned_data["deck_3"]
                deck4 = form.cleaned_data["deck_4"]
                deck5 = form.cleaned_data["deck_5"]

                list_of_decks = [
                    deck1,
                    deck2,
                    deck3,
                    deck4,
                    deck5,
                ]
                y = collections.Counter(list_of_decks)
                q = Guide(
                    name=name,
                    creator=creator,
                    description=desc,
                    Recc_Floor=recc_floor,
                )
                q.save()
                for decks in y:
                    q.required_decks.add(
                        decks, through_defaults={"deck_count": y[decks]}
                    )  # This is adding deck into RelGuide table, take note that the deck count is also added
                q.save()
                # Returns player back to guide page
                return HttpResponseRedirect(reverse("lor:Guide", args=(q.id,)))

        else:
            form = GuideMakerForm()
        context = {"form": form}
        return render(request, "LoR/guideMakingForm.html", context)
    else:
        return HttpResponseRedirect(reverse("register"))


# This is a normal view of the guide
def GuideView(request, pk):
    # Get all the decks by guide_id
    guideDecks = RelGuide.objects.filter(guide_id=pk).order_by("deck_id")
    # Get guide info by id(from pk)
    guide = Guide.objects.filter(id=pk)
    context = {"guide": guide[0], "guideDecks": guideDecks}
    return render(request, "LoR/GuideView.html", context)


# This is for the list of Guides View
class guideHomeView(generic.ListView):
    model = Guide
    template_name = "LoR/GuideHome.html"


# This is the page for the view of the deck
def deckView(request, pk):
    # Get all the cards in the deck in the RelDeck Join Table Though deck_id
    # Ordered by Cost
    deckCards = RelDeck.objects.filter(deck_id=pk).order_by("card_id__Cost")
    # Get the Deck information itself
    deck = Deck.objects.filter(id=pk)

    # Calculating The Cost of all the cards
    cost = 0.0
    for cards in deckCards:
        for i in range(cards.card_count):
            cost += cards.card_id.Cost

    avgCost = cost / 9
    avgCost = avgCost * 100
    avgCost = int(avgCost)
    avgCost = avgCost / 100

    context = {"deck": deck[0], "deckCards": deckCards, "avgCost": avgCost}
    return render(request, "LoR/deckView.html", context)


class deckSerail(generics.RetrieveAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializers


# This is the page for List of decks
def deckHomeView(request):
    # Gets all decks
    deckie = Deck.objects.all().order_by("-id").exclude(show=False)
    context = {"deckie": deckie}
    return render(request, "LoR/DeckHomeView.html", context)


# Gets the Character
class CharView(generic.DetailView):
    model = Character
    template_name = "LoR/CharacterView.html"


# Gets the view of the Page
class PageView(generic.DetailView):
    model = Page
    template_name = "LoR/PageView.html"


# Gets the list of pages
def PageList(request):
    # Gets all Pages
    p = Page.objects.all()
    # Gets all Offices
    offc = Office.objects.all()
    context = {"page": p, "offc": offc}
    return render(request, "LoR/PageList.html", context)


# Gets the list of Characters
def CharacterList(request):
    # Gets all Characters
    chars = Character.objects.all()
    # Gets all Characters without related Page
    sideChars = Character.objects.filter(Page_id=None)
    # Gets all Offices
    offc = Office.objects.all()
    context = {"chars": chars, "sideChars": sideChars, "offc": offc}
    return render(request, "LoR/CharacterList.html", context)


# This is the homepage of Ranks, display a Rank id = pk
def AbnoList(request):
    floors = Office.objects.filter(Rank=7)
    abnos = AbnoCards.objects.all()

    context = {"floors": floors, "abnos": abnos}
    return render(request, "LoR/AbnoHome.html", context)


# Abno
class AbnoView(generic.DetailView):
    model = AbnoCards
    template_name = "LoR/AbnoView.html"


class AbnoViewSet(generics.ListAPIView):

    queryset = AbnoCards.objects.all()
    serializer_class = AbnoSerializers


class EffectListView(generics.ListAPIView):
    queryset = Effects.objects.all()
    serializer_class = EffectSerializers