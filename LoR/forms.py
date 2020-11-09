from django import forms
from .models import Card, Deck
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class DeckMakerForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = "__all__"

    def clean(self):
        cards = self.cleaned_data.get("cards")
        if cards and cards.count() > 9:
            raise forms.ValidationError("Maximum 9 Cards are allowed.")

        elif cards and cards.count() < 9:
            raise forms.ValidationError("You need at least 9 cards to proceed!")
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = "post"

    cards = forms.ModelMultipleChoiceField(
        queryset=Card.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


# class DeckMakerForm(forms.Form):
#     deck_name = forms.CharField(max_length=100)
#     deck_creator = forms.CharField(max_length=100)
#     deck_description = forms.CharField(max_length=400, widget=forms.Textarea)
#     card_1 = forms.ModelChoiceField(queryset=Card.objects.all().order_by("Name"))
#     card_2 = forms.ModelChoiceField(queryset=Card.objects.all().order_by("Name"))
#     card_3 = forms.ModelChoiceField(queryset=Card.objects.all().order_by("Name"))
#     card_4 = forms.ModelChoiceField(queryset=Card.objects.all().order_by("Name"))
#     card_5 = forms.ModelChoiceField(queryset=Card.objects.all().order_by("Name"))
#     card_6 = forms.ModelChoiceField(queryset=Card.objects.all().order_by("Name"))
#     card_7 = forms.ModelChoiceField(queryset=Card.objects.all().order_by("Name"))
#     card_8 = forms.ModelChoiceField(queryset=Card.objects.all().order_by("Name"))
#     card_9 = forms.ModelChoiceField(queryset=Card.objects.all().order_by("Name"))

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper
#         self.helper.form_method = "post"
#         self.helper.layout = Layout(
#             "deck_name",
#             "deck_creator",
#             "deck_description",
#             "card_1",
#             "card_2",
#             "card_3",
#             "card_4",
#             "card_5",
#             "card_6",
#             "card_7",
#             "card_8",
#             "card_9",
#             Submit("submit", "Submit", css_class="btn-success"),
#         )