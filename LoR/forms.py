from django import forms
from .models import Card, Deck, Office, Page, Effects, Rank
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
import collections


# This is the "form" for the Guide
class GuideMakerForm(forms.Form):
    guide_name = forms.CharField(
        max_length=50, help_text="Please keep characters below 50!"
    )
    guide_description = forms.CharField(widget=forms.Textarea)
    # floor is filtered through a query where the Rank belongs to the Library
    floor = forms.ModelChoiceField(
        queryset=Office.objects.all().filter(Rank=7),
    )
    # Decks are also filtered for user to choose
    deck_1 = forms.ModelChoiceField(
        queryset=Deck.objects.all().order_by("name"),
    )
    deck_2 = forms.ModelChoiceField(
        queryset=Deck.objects.all().order_by("name"),
    )
    deck_3 = forms.ModelChoiceField(
        queryset=Deck.objects.all().order_by("name"),
    )
    deck_4 = forms.ModelChoiceField(
        queryset=Deck.objects.all().order_by("name"),
    )
    deck_5 = forms.ModelChoiceField(
        queryset=Deck.objects.all().order_by("name"),
    )

    # Checks validity of inputted data
    def clean(self):
        N = self.cleaned_data.get("deck_name")
        J = Deck.objects.filter(name=N)
        if J:
            raise forms.ValidationError("That name is taken!")
        if len(str(N)) > 50:
            raise forms.ValidationError("Your name is too long!")

    # A simple modifier to align the Form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            "guide_name",
            "guide_description",
            "floor",
            "deck_1",
            "deck_2",
            "deck_3",
            "deck_4",
            "deck_5",
            Submit("submit", "Submit", css_class="btn-success"),
        )


# This is a "form" for user to make decks
class DeckMakerForm(forms.Form):
    deck_name = forms.CharField(max_length=50)
    deck_description = forms.CharField(widget=forms.Textarea)
    # Query to only allow users to choose offices relating to the Library
    Reccomended_Floor = forms.ModelChoiceField(
        queryset=Office.objects.all().filter(Rank=7),
        required=False,
        help_text="You can leave this blank",
    )
    # Query the list of pages
    Reccomended_Page = forms.ModelChoiceField(
        queryset=Page.objects.all(),
        required=False,
        help_text="You can leave this blank",
    )

    # Query the list of Ranks
    Reccomended_Rank = forms.ModelChoiceField(
        queryset=Rank.objects.exclude(id=7).order_by("id"),
        required=False,
        help_text="What Rank/Chapter is this deck viable at?",
    )
    # Query the list of cards
    card_1 = forms.ModelChoiceField(
        queryset=Card.objects.all().order_by("Name"),
        required=True,
    )
    card_2 = forms.ModelChoiceField(
        queryset=Card.objects.all().order_by("Name"),
        required=True,
    )
    card_3 = forms.ModelChoiceField(
        queryset=Card.objects.all().order_by("Name"),
        required=True,
    )
    card_4 = forms.ModelChoiceField(
        queryset=Card.objects.all().order_by("Name"),
        required=True,
    )
    card_5 = forms.ModelChoiceField(
        queryset=Card.objects.all().order_by("Name"),
        required=True,
    )
    card_6 = forms.ModelChoiceField(
        queryset=Card.objects.all().order_by("Name"),
        required=True,
    )
    card_7 = forms.ModelChoiceField(
        queryset=Card.objects.all().order_by("Name"),
        required=True,
    )
    card_8 = forms.ModelChoiceField(
        queryset=Card.objects.all().order_by("Name"),
        required=True,
    )
    card_9 = forms.ModelChoiceField(
        queryset=Card.objects.all().order_by("Name"),
        required=True,
    )

    # Query the list of effects for user
    eff_1 = forms.ModelChoiceField(
        queryset=Effects.objects.all().order_by("Name"),
        required=False,
        help_text="Make sure this is unique!",
    )
    eff_2 = forms.ModelChoiceField(
        queryset=Effects.objects.all().order_by("Name"),
        required=False,
        help_text="Make sure this is unique!",
    )
    eff_3 = forms.ModelChoiceField(
        queryset=Effects.objects.all().order_by("Name"),
        required=False,
        help_text="Make sure this is unique!",
    )
    eff_4 = forms.ModelChoiceField(
        queryset=Effects.objects.all().order_by("Name"),
        required=False,
        help_text="Make sure this is unique!",
    )

    # This makes sure that there isn't more than 3 cards of the same id
    def clean(self):

        N = self.cleaned_data.get("deck_name")
        J = Deck.objects.filter(name=N)
        if J:
            raise forms.ValidationError("That name is taken!")
        if len(str(N)) > 50:
            raise forms.ValidationError("Your name is too long!")
        cards1 = self.cleaned_data.get("card_1")
        cards2 = self.cleaned_data.get("card_2")
        cards3 = self.cleaned_data.get("card_3")
        cards4 = self.cleaned_data.get("card_4")
        cards5 = self.cleaned_data.get("card_5")
        cards6 = self.cleaned_data.get("card_6")
        cards7 = self.cleaned_data.get("card_7")
        cards8 = self.cleaned_data.get("card_8")
        cards9 = self.cleaned_data.get("card_9")
        list_of_card = [
            cards1,
            cards2,
            cards3,
            cards4,
            cards5,
            cards6,
            cards7,
            cards8,
            cards9,
        ]
        y = collections.Counter(list_of_card)
        for x in y:
            if y[x] > 3:
                raise forms.ValidationError(
                    "You can't have more than a multiple of 3 cards!"
                )
        return self.cleaned_data

    # Form alignment, not important
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            "deck_name",
            "deck_description",
            "Reccomended_Floor",
            "Reccomended_Page",
            "Reccomended_Rank",
            "card_1",
            "card_2",
            "card_3",
            "card_4",
            "card_5",
            "card_6",
            "card_7",
            "card_8",
            "card_9",
            "eff_1",
            "eff_2",
            "eff_3",
            "eff_4",
            Submit("submit", "Submit", css_class="btn-success"),
        )
