from django.db import models


def lownst(text):
    text = text.lower()
    text = text.replace(" ", "")
    return text


class Books(models.Model):
    ISBN = models.BigIntegerField(primary_key = True)
    title = models.CharField(max_length = 100)
    synopsis = models.CharField(max_length=200, blank = True, null = True)
    publication_date = models.DateField()
    edition = models.IntegerField(blank = True, null = True)
    price = models.FloatField(blank = True, null = True)
    cover = models.ImageField(upload_to =  "books", blank = True, null = True)
    active = models.BooleanField(default = True)
    
    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
        
        def __str__(self):
            return self.title
    
    def __str__(self):
        return str(self.ISBN) + " | " + self.title + " | " + str(self.active)


class Authors(models.Model):
    name = models.CharField(max_length = 50)
    middle_name = models.CharField(max_length = 10, blank = True, null = True)
    surname = models.CharField(max_length = 100)
    nickname = models.CharField(max_length = 25)
    day_birth = models.DateField()
    id = models.IntegerField(primary_key = True)
    active = models.BooleanField(default = True)
    
    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'
        
        def __str__(self):
            return self.name
        
        
    def __str__(self):
        if self.middle_name == None:
            return str(self.id) + " | " + self.name + " | " + self.surname + " | " + " | " + str(self.active)
        else:
            return str(self.id) + " | " + self.name + " | " + self.middle_name + " | " + self.surname + " | " + " | " + str(self.active)


class Editorials(models.Model):
    name = models.CharField(max_length = 50)
    founder = models.CharField(max_length = 50, blank = True, null = True)
    foundation_date = models.DateField(blank = True, null = True)
    country = models.CharField(max_length = 50, blank = True, null = True)
    main_organization = models.CharField(max_length = 50, blank = True, null = True)
    id = models.IntegerField(primary_key = True)    
    active = models.BooleanField(default = True)
    
    class Meta:
        verbose_name = 'editorial'
        verbose_name_plural = 'editorials'
        
        def __str__(self):
            return self.name
        
    def __str__(self):
        return str(self.id) + " | " + self.name + " | " + str(self.id) + " | " + str(self.active)


class Genres(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100, blank = True, null = True)
    id = models.IntegerField(primary_key = True)   
    active = models.BooleanField(default = True)

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'
        
        def __str__(self):
            return self.name
    
    def __str__(self):
        return str(self.id) + " | " + self.name + " | " + str(self.active)
