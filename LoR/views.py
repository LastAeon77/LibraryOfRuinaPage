from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Office, Rank, Card
from .forms import DeckMakerForm


class IndexView(generic.ListView):
    pass


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
            SELECT O.Rank_id AS id,R.`Name`, COUNT(*) AS rank_num, R.slug
            FROM lor_office AS O INNER JOIN lor_rank AS R ON O.Rank_id = R.id
            GROUP BY O.`Rank_id`
            ORDER BY O.id"""
    )

    context = {"Office": Offc, "Counting": NumberOfOff}
    return render(request, "LoR/OfficeHome.html", context)


def CardDetailView(request, slug):

    Page = Card.objects.raw(
        f"""SELECT C.*, R.`Name` AS `Rank`, O.`Name` AS off,R.ImgPath AS RankImg, O.ImgPath AS OffImg
            FROM lor_office AS O,lor_card AS C,lor_rank AS R
            WHERE R.id = O.rank_id AND O.id = C.Office_id AND C.slug = '{slug}' """
    )
    context = {"card": Page[0]}
    return render(request, "LoR/CardDetail.html", context)


def CardHomeView(request):
    Cards = Card.objects.all()
    Offices = Card.objects.raw(
        """SELECT O.id,O.Rank_id,O.`Name`AS OfficeName,COUNT(*) AS NumberOfCards
FROM (lor_office AS O INNER JOIN lor_card AS C ON O.id = C.Office_id)
GROUP BY O.id
ORDER BY O.id
"""
    )
    Ranks = Card.objects.raw(
        """SELECT R.id AS id,R.`Name`AS RankName,COUNT(*) AS NumberOfOffices, R.slug
            FROM (lor_office AS O LEFT JOIN lor_rank AS R ON O.Rank_id = R.id)
            GROUP BY R.id
            """
    )
    context = {"card": Cards, "office": Offices, "rank": Ranks}
    return render(request, "LoR/CardHome.html", context)


def deck_maker_form(request):
    if request.method == "POST":
        form = DeckMakerForm(request.POST)
        if form.is_valid():
            deck_name = form.cleaned_data["deck_name"]
            deck_creator = form.cleaned_data["deck_creator"]
            deck_description = form.cleaned_data["deck_description"]
            print(deck_name, deck_creator, deck_description)

    form = DeckMakerForm()
    context = {"form": form}
    return render(request, "LoR/deckMakingForm.html", context)
