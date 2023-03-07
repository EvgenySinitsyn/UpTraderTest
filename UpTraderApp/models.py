from django.db import models


class MenuItem(models.Model):
    name = models.CharField("Название", max_length=100)
    slug = models.SlugField("Ссылка", max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children',
                               verbose_name="Родитель")
    depth = models.PositiveIntegerField('Глубина', default=0)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
