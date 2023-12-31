from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True)
    description = models.TextField()
    rating = models.PositiveIntegerField(null=True,)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    release_date = models.DateField(auto_now_add=True, null=True)
    players = models.PositiveIntegerField(null=True,)
    on_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Console(Product):
    colour = models.CharField(max_length=100, null=True)
    manufacturer = models.CharField(max_length=254, null=True,)
    storage = models.CharField(max_length=254, null=True,)


class Game(Product):
    developer = models.CharField(max_length=254, null=True,)
    publisher = models.CharField(max_length=254, null=True,)
    pgi_certificate = models.CharField(max_length=254, null=True, blank=True)
    CONSOLE_CHOICES = (
        ('Playstation_one', 'Playstation One'),
        ('Playstation_two', 'Playstation Two'),
        ('Playstation_portable', 'Playstation Portable (PSP)'),
        ('Nintendo_snes', 'Super Nintendo (SNES)'),
        ('Nintendo_64', 'Nintendo 64'),
        ('Nintendo_gamecube', 'Nintendo GameCube'),
        ('Sega_genesis', 'Sega Genesis'),
        ('Gameboy_advanced', 'Gameboy Advanced'),
    )
    platform = models.CharField(
        max_length=50,
        choices=CONSOLE_CHOICES,
        null=True,
        )
    GENRE_CHOICES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('RPG', 'Role-Playing Game'),
        ('Simulation', 'Simulation'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Puzzle', 'Puzzle'),
        ('Platformer', 'Platformer'),
        ('Fighting', 'Fighting'),
        ('Horror', 'Horror'),
        ('Racing', 'Racing'),
    )
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, null=True,)
