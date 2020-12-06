from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from LoR.models import Deck


# Register page
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get("username")
            messages.success(
                request, "Your account has been created! You have been logged in."
            )
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {"form": form})


# Profile page, not much
# However, does include the list of decks created by that user, Queried
@login_required
def profile(request):
    deck_data = Deck.objects.all().filter(creator=request.user.id)
    context = {"user": request.user, "deck": deck_data}
    return render(request, "users/profile.html", context)


# class DeckDelete(DeleteView):
#     model = Deck
#     success_url = reverse_lazy("lor:DeckHome")


# message.debug
# message.info
# message.success
# message.warning
# message.error
