from django.db import models


class AddressManager(models.Manager):
    def get_by_natural_key(self, country, city, street):
        return self.get(country=country, city=city, street=street)


class Address(models.Model):
    objects = AddressManager()

    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=100)

    def __str__(self):
        return self.street + ". " + self.city + ", " + self.country + "."

    class Meta:
        unique_together = (('country', 'city', 'street'),)


class NameManager(models.Manager):
    def get_by_natural_key(self, title, first_name, last_name):
        return self.get(title=title, first_name=first_name, last_name=last_name)


class Name(models.Model):
    objects = NameManager()

    title = models.CharField(max_length=6, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return (self.title + " " if self.title and len(self.title) > 0 else "") + self.first_name + " " + self.last_name

    class Meta:
        unique_together = (('title', 'first_name', 'last_name'),)


class Person(models.Model):
    name = models.ForeignKey(Name, on_delete=models.PROTECT)
    phone = models.CharField(max_length=20)
    avatar_image = models.CharField(max_length=200)
    avatar_origin = models.URLField(max_length=200)
    email = models.EmailField(max_length=200)
    quote = models.CharField(max_length=500)
    chuck = models.CharField(max_length=500)
    birthday = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.PROTECT)

    def __str__(self):
        return self.avatar_image
