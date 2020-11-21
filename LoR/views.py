from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Office, Rank, Card, Deck, RelDeck, Page, Character, Guide, RelGuide
from .forms import DeckMakerForm, GuideMakerForm
from django.urls import reverse
import collections
from django.contrib.auth.decorators import login_required


def HomePage(request):
    return render(request, "LoR/LoRHomePage.html")


class OfficeView(generic.DetailView):
    model = Office
    template_name = "LoR/OfficeDetail.html"


class RankView(generic.DetailView):
    model = Rank
    template_name = "LoR/RankDetail.html"


def OfficeHomePage(request):
    Offc = Office.objects.all()
    # cursor = connection.cursor()
    # cursor.execute("""use library_of_ruina;
    #         SELECT O.Rank_id,R.`Name`, COUNT(*) AS rank_num
    #         FROM lor_office AS O INNER JOIN lor_rank AS R ON O.Rank_id = R.id
    #         GROUP BY O.`Rank_id`""")
    # results = cursor.fetchall()
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


def CardDetailView(request, slug):

    pag = Card.objects.raw(
        f"""SELECT C.*, R."Name" AS "Rank", O."Name" AS "off",R."ImgPath" AS "RankImg", O."ImgPath" AS "OffImg"
FROM "LoR_office" AS O , "LoR_card" AS C,"LoR_rank" AS R
WHERE R."id" = O."Rank_id" AND O."id" = C."Office_id" AND C."slug" = '{slug}'"""
    )
    context = {"card": pag[0]}
    return render(request, "LoR/CardDetail.html", context)


def CardHomeView(request):
    Cards = Card.objects.all()
    Offices = Card.objects.raw(
        """SELECT O."id",O."Rank_id",O."Name" AS "OfficeName",COUNT(*) AS "NumberOfCards"
FROM ("LoR_office" AS O INNER JOIN "LoR_card" AS C ON O."id" = C."Office_id")
GROUP BY O."id"
ORDER BY O."id"
"""
    )
    Ranks = Card.objects.raw(
        """SELECT R.id AS id,R."Name" AS RankName,COUNT(*) AS NumberOfOffices, R.slug
FROM ("LoR_office" AS O LEFT JOIN "LoR_rank" AS R ON O."Rank_id" = R."id")
GROUP BY R."id"
ORDER BY R."id"
            """
    )
    context = {"card": Cards, "office": Offices, "rank": Ranks}
    return render(request, "LoR/CardHome.html", context)


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
                card1 = form.cleaned_data["card_1"]
                card2 = form.cleaned_data["card_2"]
                card3 = form.cleaned_data["card_3"]
                card4 = form.cleaned_data["card_4"]
                card5 = form.cleaned_data["card_5"]
                card6 = form.cleaned_data["card_6"]
                card7 = form.cleaned_data["card_7"]
                card8 = form.cleaned_data["card_8"]
                card9 = form.cleaned_data["card_9"]
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
                )
                q.save()
                eff_1 = form.cleaned_data["eff_1"]
                eff_2 = form.cleaned_data["eff_2"]
                eff_3 = form.cleaned_data["eff_3"]
                eff_4 = form.cleaned_data["eff_4"]

                eff_list = [eff_1, eff_2, eff_3, eff_4]
                eff_list = list(dict.fromkeys(eff_list))
                for effs in eff_list:
                    q.effect.add(effs)
                for cards in y:
                    q.cards.add(cards, through_defaults={"card_count": y[cards]})
                q.save()
                # form.save()
                return HttpResponseRedirect(reverse("lor:Deck", args=(q.id,)))

        else:
            form = DeckMakerForm()
        context = {"form": form}
        return render(request, "LoR/deckMakingForm.html", context)
    else:
        return HttpResponseRedirect(reverse("register"))


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
                    )
                q.save()
                # form.save()
                return HttpResponseRedirect(reverse("lor:Guide", args=(q.id,)))

        else:
            form = GuideMakerForm()
        context = {"form": form}
        return render(request, "LoR/guideMakingForm.html", context)
    else:
        return HttpResponseRedirect(reverse("register"))


def GuideView(request, pk):
    guideDecks = RelGuide.objects.filter(guide_id=pk).order_by("deck_id")
    guide = Guide.objects.filter(id=pk)
    context = {"guide": guide[0], "guideDecks": guideDecks}
    return render(request, "LoR/GuideView.html", context)


class guideHomeView(generic.ListView):
    model = Guide
    template_name = "LoR/GuideHome.html"


def deckView(request, pk):
    deckCards = RelDeck.objects.filter(deck_id=pk).order_by("card_id__Cost")
    deck = Deck.objects.filter(id=pk)
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


def deckHomeView(request):
    deckie = Deck.objects.all()
    context = {"deckie": deckie}
    return render(request, "LoR/DeckHomeView.html", context)


class CharView(generic.DetailView):
    model = Character
    template_name = "LoR/CharacterView.html"


class PageView(generic.DetailView):
    model = Page
    template_name = "LoR/PageView.html"


def PageList(request):
    p = Page.objects.all()
    offc = Office.objects.all()
    context = {"page": p, "offc": offc}
    return render(request, "LoR/PageList.html", context)


def CharacterList(request):
    chars = Character.objects.all()
    sideChars = Character.objects.filter(Page_id=None)
    offc = Office.objects.all()
    context = {"chars": chars, "sideChars": sideChars, "offc": offc}
    return render(request, "LoR/CharacterList.html", context)
