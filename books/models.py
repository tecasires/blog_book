from django.db import models


def lownst(text):
    text = text.lower()
    text = text.replace(" ", "")
    return text


class Books(models.Model):
    ISBN = models.BigIntegerField(primary_key = True)
    title = models.CharField(max_length = 100)
    synopsis = models.CharField(max_length=200, blank = True, null = True)
    publication_date = models.DateField
    edition = models.IntegerField
    price = models.FloatField()
    cover = models.ImageField(upload_to =  "books", null = True)
    active = models.BooleanField(default = True)
    
    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
    
    def __str__(self):
        return str(self.ISBN) + " | " + self.title + " | " + str(self.active)


class Authors(models.Model):
    name = models.CharField(max_length = 50, null = False)
    middle_name = models.CharField(max_length = 10)
    surname = models.CharField(max_length = 100, null = False)
    nickname = models.CharField(max_length = 25)
    day_birth = models.DateField
    id = models.IntegerField(primary_key = True)
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'
        
    def __str__(self):
        return self.name + " | " + self.middle_name + " | " + self.surname + " | " + str(self.price) + " | " + str(self.active)


class Editorials(models.Model):
    name = models.CharField(max_length = 50, null = False)
    founder = models.CharField(max_length = 50, null = False)
    foundation_date = models.DateField
    country = models.CharField(max_length = 50, null = False)
    main_organization = models.CharField(max_length = 50, null = False)
    id = models.IntegerField(primary_key = True)    
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'editorial'
        verbose_name_plural = 'editorials'
        
    def __str__(self):
        return self.name + " | " + self.founder + " | " + self.main_organization + " | " + str(self.active)


class Genres(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    id = models.IntegerField(primary_key = True)   
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'
    
    def __str__(self):
        return self.name + " | " + self.description + " | " + str(self.active)
