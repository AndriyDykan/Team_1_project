from django.db import models

class Image(models.Model):
    class_choices = [
        (1, 'airplane'),
        (2, 'automobile'),
        (3, 'bird'),
        (4, 'cat'),
        (5, 'deer'),
        (6, 'dog'),
        (7, 'frog'),
        (8, 'horse'),
        (9, 'ship'),
        (10, 'truck'),
    ]
    image_class = models.IntegerField(choices=class_choices)
    image_predicted_class = models.IntegerField(choices=class_choices)
    image = models.ImageField(upload_to="img")

    def __str__(self):
        return f"{self.get_image_class_display()} - {self.id}"

    def save(self, *args, **kwargs):
        # Код для передбачення класу зображення

        self.image_predicted_class = 1

        # Виклик оригінального методу save
        super().save(*args, **kwargs)