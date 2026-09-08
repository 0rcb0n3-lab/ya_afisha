from django.db import models
from django.urls import reverse


class Place(models.Model):
    title = models.CharField('Title', max_length=200)
    short_description = models.TextField('Short description', blank=True)
    long_description = models.TextField('Full description', blank=True)
    lng = models.FloatField('Longitude')
    lat = models.FloatField('Latitude')

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    def __str__(self) -> str:
        return self.title

    def as_feature(self) -> dict:
        return {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [self.lng, self.lat],
            },
            "properties": {
                "title": self.title,
                "placeId": self.pk,
                "detailsUrl": reverse("place_detail", kwargs={"pk": self.pk}),
            },
        }

    def as_json(self) -> dict:
        return {
            "title": self.title,
            "imgs": [img.image.url for img in self.images.all()],
            "description_short": self.short_description,
            "description_long": self.long_description,
            "coordinates": {
                "lat": self.lat,
                "lng": self.lng,
            },
        }


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.ImageField('Picture', upload_to='places_images')
    ordering = models.PositiveIntegerField('Order', default=0)

    class Meta:
        ordering = ['ordering']
        verbose_name = 'Place image'
        verbose_name_plural = 'Places images'

    def __str__(self) -> str:
        return f'{self.place.title} - image {self.ordering}'
