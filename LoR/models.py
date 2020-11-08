from django.db import models
from django.utils.translation import gettext_lazy as laz


class Rank(models.Model):
    Name = models.CharField(max_length=30, unique=True)
    Slogan = models.CharField(max_length=200)
    Description = models.TextField(max_length=30)
    ImgPath = models.CharField(max_length=300)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.Name


class Office(models.Model):
    Name = models.CharField(max_length=200, unique=True)
    Info = models.TextField()
    Rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    ImgPath = models.CharField(max_length=300)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.Name


class Effects(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.TextField()
    InGameId = models.IntegerField(unique=True)


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
    InitialEffects = models.ManyToManyField(Effects)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.Name


class Character(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    Story = models.TextField(null=True)
    Office = models.ForeignKey(Office, on_delete=models.CASCADE)
    Page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True)
    ImgPath = models.CharField(max_length=300, null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.Name


class Rel_Page_Eff(models.Model):
    Effects = models.ForeignKey(Effects, on_delete=models.CASCADE)
    Page = models.ForeignKey(Page, on_delete=models.CASCADE)


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

    class Types(models.TextChoices):
        BLUNT = "BL", laz("Blunt")
        PIERCE = "PI", laz("Pierce")
        SLASH = "SL", laz("Slash")
        EVADE = "EV", laz("Evade")
        BLOCK = "BO", laz("Block")

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
        max_length=2, choices=Types.choices, null=True, blank=True, default=None
    )
    Roll2 = models.CharField(max_length=10, null=True, blank=True)
    Eff2 = models.CharField(max_length=200, null=True, blank=True)
    Type2 = models.CharField(
        max_length=2, choices=Types.choices, null=True, blank=True, default=None
    )
    Roll3 = models.CharField(max_length=10, null=True, blank=True)
    Eff3 = models.CharField(max_length=200, null=True, blank=True)
    Type3 = models.CharField(
        max_length=2, choices=Types.choices, null=True, blank=True, default=None
    )
    Roll4 = models.CharField(max_length=10, null=True, blank=True)
    Eff4 = models.CharField(max_length=200, null=True, blank=True)
    Type4 = models.CharField(
        max_length=2, choices=Types.choices, null=True, blank=True, default=None
    )
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.Name


class Deck(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    Creator = models.CharField(max_length=100)
    Description = models.CharField(max_length=400)

    def __str__(self):
        return self.Name


class RelDeck(models.Model):
    deck_id = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card_id = models.ForeignKey(Card, on_delete=models.CASCADE)
