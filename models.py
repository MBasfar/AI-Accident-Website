from django.db import models

class Accident(models.Model):
    accident_id = models.CharField(max_length=20, unique=True)
    name_A = models.CharField(max_length=30)
    national_idA = models.CharField(max_length=10)
    vehicle_typeA = models.CharField(max_length=30)
    plate_A = models.CharField(max_length=10)
    license_A = models.CharField(max_length=10)

    name_B = models.CharField(max_length=30)
    national_idB = models.CharField(max_length=10)
    vehicle_typeB = models.CharField(max_length=30)
    plate_B = models.CharField(max_length=10)
    license_B = models.CharField(max_length=10)


    
    image_a = models.ImageField(upload_to='accident_photos/')
    image_b = models.ImageField(upload_to='accident_photos/')

    feature_1 = models.FloatField(max_length=2)

    feature_2 = models.FloatField(max_length=2)
    feature_3 = models.FloatField(max_length=2)
    feature_4 = models.FloatField(max_length=2)

    feature_5 = models.BooleanField(default=False)
    feature_6 = models.BooleanField(default=False)
    feature_7 = models.BooleanField(default=False)
    feature_8 = models.BooleanField(default=False)
    feature_9 = models.BooleanField(default=False)
    feature_10 = models.BooleanField(default=False)
    feature_11 = models.BooleanField(default=False)
    feature_12 = models.BooleanField(default=False)
    feature_13 = models.BooleanField(default=False)
    feature_14 = models.BooleanField(default=False)
    status = models.CharField(max_length=10, default='Pending', choices=[('Accepted', 'Accepted'), ('Objected', 'Objected'), ('Pending', 'Pending')])
    liableA = models.CharField(max_length=6, default="0")
    liableB = models.CharField(max_length=6, default="0")
