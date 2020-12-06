from django.db import models
from django.utils.translation import gettext_lazy as laz
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


# model for Ranks
class Rank(models.Model):
    Name = models.CharField(max_length=30, unique=True)
    Slogan = models.CharField(max_length=200)
    Description = models.TextField()
    ImgPath = models.CharField(max_length=300)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.Name


# model for Offices
class Office(models.Model):
    Name = models.CharField(max_length=200, unique=True)
    Info = models.TextField()
    Rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    ImgPath = models.CharField(max_length=300)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.Name


# model for Effects
class Effects(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.TextField()
    InGameId = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.Name}: {self.Description}"


# model for Page
class Page(models.Model):
    Name = models.CharField(max_length=200, unique=True)
    Story = models.TextField()
    InGameId = models.IntegerField(unique=True)

    class RarityChoice(models.TextChoices):
        PAPERBACK = "P", laz("Paperback")
        LIMITED = "L", laz("Limited")
        HARDCOVER = "H", laz("Hardcover")
        OBJETDART = "O", laz("Objet d'art")
        EGO = "E", laz("EGO")

    Rarity = models.CharField(
        max_length=1,
        choices=RarityChoice.choices,
        default=RarityChoice.PAPERBACK,
        null=True,
    )
    InitialEffects = models.ManyToManyField(Effects, blank=True)
    slug = models.SlugField(null=True)
    Office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True)
    HP = models.IntegerField(blank=True, null=True)
    Stagger = models.IntegerField(blank=True, null=True)
    SpeedMin = models.IntegerField(blank=True, null=True)
    Speed = models.IntegerField(blank=True, null=True)
    SlashResist = models.CharField(max_length=100, default="Normal")
    PierceResist = models.CharField(max_length=100, default="Normal")
    BluntResist = models.CharField(max_length=100, default="Normal")
    SlashStaggerResist = models.CharField(max_length=100, default="Normal")
    PierceStaggerResist = models.CharField(max_length=100, default="Normal")
    BluntStaggerResist = models.CharField(max_length=100, default="Normal")
    RangeType = models.CharField(max_length=100, blank=True, null=True)
    SpeedDiceNum = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.Name

    def story_as_list(self):
        return self.Story.splitlines()


# model for Characters
class Character(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    Story = models.TextField(null=True)
    Page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True)
    ImgPath = models.CharField(max_length=300, null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.Name


# model for Card
class Card(models.Model):
    Name = models.CharField(max_length=200, unique=True)

    class RarityChoice(models.TextChoices):
        PAPERBACK = "P", laz("Paperback")
        HARDCOVER = "H", laz("Hardcover")
        LIMITED = "L", laz("Limited")
        OBJETDART = "O", laz("Objet d'art")
        EGO = "E", laz("EGO")

    Rarity = models.CharField(
        max_length=1,
        choices=RarityChoice.choices,
        default=RarityChoice.PAPERBACK,
        null=True,
    )
    Obtainable = models.BooleanField(default=True)
    Cost = models.IntegerField()
    On_Play_Effect = models.TextField(null=True, blank=True)
    Dice_Number = models.IntegerField(null=True)
    Office = models.ForeignKey(Office, on_delete=models.CASCADE)
    ImgPath = models.CharField(max_length=300, null=True)
    Roll1 = models.CharField(max_length=10, null=True, blank=True)
    Eff1 = models.CharField(max_length=200, null=True, blank=True)

    # Class to restirct available choices for the box
    class Types(models.TextChoices):
        BLUNT = "BL", laz("Blunt")
        PIERCE = "PI", laz("Pierce")
        SLASH = "SL", laz("Slash")
        EVADE = "EV", laz("Evade")
        BLOCK = "BO", laz("Block")

    # Restrict type of Card
    class CardTypes(models.TextChoices):
        MELEE = "M", laz("Melee")
        RANGED = "R", laz("Ranged")

    CardType = models.CharField(
        max_length=1,
        choices=CardTypes.choices,
        null=True,
        blank=True,
        default=CardTypes.MELEE,
    )

    Type1 = models.CharField(
        max_length=2,
        choices=Types.choices,
        null=True,
        blank=True,
        default=None,
    )
    Roll2 = models.CharField(max_length=10, null=True, blank=True)
    Eff2 = models.CharField(max_length=200, null=True, blank=True)
    Type2 = models.CharField(
        max_length=2,
        choices=Types.choices,
        null=True,
        blank=True,
        default=None,
    )
    Roll3 = models.CharField(max_length=10, null=True, blank=True)
    Eff3 = models.CharField(max_length=200, null=True, blank=True)
    Type3 = models.CharField(
        max_length=2,
        choices=Types.choices,
        null=True,
        blank=True,
        default=None,
    )
    Roll4 = models.CharField(max_length=10, null=True, blank=True)
    Eff4 = models.CharField(max_length=200, null=True, blank=True)
    Type4 = models.CharField(
        max_length=2,
        choices=Types.choices,
        null=True,
        blank=True,
        default=None,
    )
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.Name

    def getid(self):
        return self.pk


# model for decks
class Deck(models.Model):
    name = models.CharField(max_length=50, unique=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    description = models.TextField()
    cards = models.ManyToManyField(Card, through="RelDeck")
    Recc_Floor = models.ForeignKey(
        Office, on_delete=models.CASCADE, null=True, blank=True
    )
    Recc_Page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    effect = models.ManyToManyField(Effects)

    def __str__(self):
        return self.name

    def description_as_list(self):
        return self.description.splitlines()


# join table for deck and cards
class RelDeck(models.Model):
    deck_id = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card_id = models.ForeignKey(Card, on_delete=models.CASCADE)
    card_count = models.IntegerField(
        validators=[MaxValueValidator(4), MinValueValidator(0)]
    )

    def __str__(self):
        return self.deck_id.name


# guide model
class Guide(models.Model):
    name = models.CharField(max_length=50, unique=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    description = models.TextField()
    Recc_Floor = models.ForeignKey(
        Office, on_delete=models.CASCADE, null=True, blank=True
    )
    required_decks = models.ManyToManyField(Deck, through="RelGuide")

    def __str__(self):
        return self.name

    def description_as_list(self):
        return self.description.splitlines()


# the join table for Guide and decks
class RelGuide(models.Model):
    guide_id = models.ForeignKey(Guide, on_delete=models.CASCADE)
    deck_id = models.ForeignKey(Deck, on_delete=models.CASCADE)
    deck_count = models.IntegerField(
        validators=[MaxValueValidator(6), MinValueValidator(0)]
    )

    def __str__(self):
        return self.guide_id.name
