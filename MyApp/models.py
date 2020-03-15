from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        name = self.first_name + self.last_name
        return name


class Album(models.Model):
    """唱片"""
    """ on_delete=models.CASCADE 联级删除 """
    artist = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField(default=0)

    def __str__(self):
        return self.name


