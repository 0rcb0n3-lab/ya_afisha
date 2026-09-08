from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    short_description = models.TextField('Короткое описание', blank=True)
    long_description = models.TextField('Полное описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self) -> str:
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место',
    )
    image = models.ImageField('Изображение', upload_to='places_images')
    ordering = models.PositiveIntegerField('Номер по порядку', default=0)

    class Meta:
        ordering = ['ordering']
        verbose_name = 'Изображение места'
        verbose_name_plural = 'Изображения мест'

    def __str__(self) -> str:
        return f'{self.place.title} - image {self.ordering}'
