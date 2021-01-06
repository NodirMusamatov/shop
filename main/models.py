from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Slider(models.Model):
    main_title = models.CharField(max_length=300, blank=True)
    photo = models.ImageField(upload_to='upload')
    mini_description = models.CharField(max_length=500, blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.main_title



class Review(models.Model):
    photo = models.ImageField(upload_to='upload')
    rating = models.IntegerField(default=0)
    last_name = models.CharField(max_length=300)
    first_name = models.CharField(max_length=300)
    position = models.CharField(max_length=300)
    short_description = models.CharField(max_length=600)
    status = models.IntegerField(default=0)
    is_main = models.IntegerField(default=0)


    def __str__(self):
        return self.last_name



class Category(models.Model):
    title = models.CharField(max_length=300)
    status = models.IntegerField(default=0)
    is_main = models.BooleanField(default=0, blank=True)

    def __str__(self):
        return self.title

class Size(models.Model):
    title = models.CharField(max_length=300, blank=True)
    status = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title

class Menu(models.Model):
    title = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    photo = models.ImageField(upload_to='upload')
    old_price = models.FloatField(max_length=300, default=0, blank=True)
    new_price = models.FloatField(max_length=300, default=0)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    photo1 = models.ImageField(upload_to='upload', blank=True)
    photo2 = models.ImageField(upload_to='upload', blank=True)
    photo3 = models.ImageField(upload_to='upload', blank=True)
    is_best_seller = models.BooleanField(default=0, blank=True)
    is_rebate = models.BooleanField(default=0, blank=True)
    is_new = models.BooleanField(default=0, blank=True)
    tags = models.CharField(max_length=300)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    rebate = models.IntegerField(default=0, blank=True)
    recipe = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Cheff(models.Model):
    photo = models.ImageField(upload_to='upload')
    last_name = models.CharField(max_length=300)
    first_name = models.CharField(max_length=300)
    position = models.CharField(max_length=300)
    mini_description = models.CharField(max_length=300)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    facebook = models.CharField(max_length=300, blank=True)
    whatsapp = models.CharField(max_length=300, blank=True)
    twitter = models.CharField(max_length=300, blank=True)
    signature = models.ImageField(upload_to='upload', blank=True)



    def __str__(self):
        return self.last_name

class Award(models.Model):
    logo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    year = models.CharField(max_length=300, blank=True)
    mini_description = models.CharField(max_length=300, blank=True)
    cheff = models.ForeignKey(Cheff, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Partner(models.Model):
    name = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)


    def __str__(self):
        return self.name


class Register(models.Model):
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)
    # status = models.IntegerField(default=0)
    message = models.TextField()

    def __str__(self):
        return self.name


class Information(models.Model):
    logo = models.ImageField(upload_to='upload', blank=True)
    address = models.CharField(max_length=300, blank=True)
    phone_info = models.CharField(max_length=300, blank=True)
    baker_info = models.TextField(blank=True)
    footer_info = models.CharField(max_length=300, blank=True)
    footer_photo = models.ImageField(upload_to='upload', blank=True)
    about_info = models.CharField(max_length=300, blank=True)
    card_info = models.ImageField(upload_to='upload', blank=True)
    card_info1 = models.ImageField(upload_to='upload', blank=True)
    card_info2 = models.ImageField(upload_to='upload', blank=True)
    card_info3 = models.ImageField(upload_to='upload', blank=True)
    date_info = models.CharField(max_length=300, blank=True)
    time_info = models.CharField(max_length=300, blank=True)
    contact_info = models.CharField(max_length=300, blank=True)
    facebook_info = models.CharField(max_length=300, blank=True)
    instagram_info = models.CharField(max_length=300, blank=True)
    whatsapp_info = models.CharField(max_length=300, blank=True)
    app_store = models.CharField(max_length=300, blank=True)
    order_info = models.CharField(max_length=300, blank=True)
    order_info1 = models.CharField(max_length=300, blank=True)
    order_info2 = models.CharField(max_length=300, blank=True)
    order_info3 = models.CharField(max_length=300, blank=True)
    reviews_foto = models.ImageField(upload_to='upload', blank=True)
    design_by = models.CharField(max_length=300, blank=True)
    status = models.IntegerField(default=0, blank=True)
    banner1 = models.ImageField(upload_to='upload', blank=True)
    banner2 = models.ImageField(upload_to='upload', blank=True)




    def __str__(self):
        return self.address















