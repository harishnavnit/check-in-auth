from django.db import models


class Hubspot(models.Model):
    hubspot_name = models.CharField(max_length=200)
    hubspot_map_location = models.FloatField()
    hubspot_popularity = models.IntegerField()
    hubspot_category = (
        ('AIR', 'airport'),
        ('AM_PARK', 'amusement_park'), ('AQ', 'aquarium'),
        ('ART_GAL', 'art_gallery'), ('BAR', 'bar'), ('CH', 'church'),
        ('CAS', 'casino'), ('CAF', 'cafe'), ('MT', 'movie_theater'),
        ('NC', 'night_club'), ('SM', 'shopping_mall'),
        ('STAD', 'stadium'), ('STR', 'store'), ('SUB', 'subway_Station'),
        ('TRAIN', 'train_station'), ('TRANSIT', 'transit_station'),
        ('ZOO', 'zoo')
    )

    def __str__(self):
        return self.hubspot_name
