from django.db import models

class Shape(models.Model):
    sides = models.PositiveIntegerField()

    def save(self):
        created = self.pk is None
        super(Shape).save()
        if created:
            for i in range(self.sides):
                Coordinate.objects.create(shape_id=self.id)


class Coordinate(models.Model):
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE, related_name='coordinates')
    x_axis = models.FloatField(default=0)
    y_axis = models.FloatField(default=0)
