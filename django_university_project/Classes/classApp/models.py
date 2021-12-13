from django.db import models
#Created the Database Model
class djangoClasses (models.Model):
    title = models.CharField (max_length = 50, blank= False, null= False )
    courseNumber= models.IntegerField (max_length = 10, blank=False)
    instructorName = models.CharField (max_length = 30, blank =True, null=True)
    duration = models.FloatField(max_length = 5, blank=False, null=False)

    objects= models.Manager()
#Used the str method to return the object readable to the user
    def __str__(self):
        return self.title