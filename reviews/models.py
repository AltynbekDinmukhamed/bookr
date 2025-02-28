from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)

#exsersize 3.03


from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    author = models.CharField(max_length=255, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    published_date = models.DateField(verbose_name="Дата публикации", blank=True, null=True)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True, verbose_name="Обложка")

    def __str__(self):
        return self.title
