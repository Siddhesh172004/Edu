from django.db import models
from django.db.models.base import Model, ModelBase
from django.utils import timezone

# shop Content  are  here.
class Ecomapp11(models.Model):
    course_id=models.AutoField
    name=models.CharField(max_length=25)
    desc=models.CharField(max_length=500)
    price=models.IntegerField()
    image = models.ImageField(upload_to="courseapp\images",default="courseapp\images\shoe.jpg")
    pub_date = models.DateField(default=timezone.now)
    extra_details=models.CharField(max_length=500,default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries")
    category=models.CharField(max_length=25,default="Daily use")
    # name=models.CharField(max_length=25)

    def __str__(self):
        return self.name


# shop Content  are  here.
class Contact(models.Model):
    course_id=models.AutoField
    Name=models.CharField(max_length=25)
    Email=models.CharField(max_length=50)
    Tel=models.IntegerField()
    Image = models.ImageField(upload_to="contact\images",default="contact\images\shoe.jpg")
    pub_date = models.DateField(default=timezone.now)
    Desc=models.CharField(max_length=500)
    # name=models.CharField(max_length=25)

    def __str__(self):
        return self.Name

        
class order(models.Model):
    jsonCart = models.CharField(max_length=200,default="")
    email = models.CharField(max_length=50,default="")
    first_name =  models.CharField(max_length=50,default="")
    state =  models.CharField(max_length=50,default="")
    isSameBillingAddress = models.BooleanField(default=False)
    last_name =  models.CharField(max_length=50)
    address =  models.CharField(max_length=200)
    zip = models.IntegerField()
    order_date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.email

# shop Content  are  here.
class Ownshop(models.Model):
    title1=models.CharField(max_length=25)
    desc1=models.CharField(max_length=500)
    price1=models.IntegerField()
    image1 = models.ImageField(upload_to="Blog\images",default="courseapp\images\shoe.jpg")
    pub_date1 = models.DateField(default=timezone.now)
    # name=models.CharField(max_length=25)

    def __str__(self):
        return self.title1
