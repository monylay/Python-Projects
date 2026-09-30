from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default='', blank=True, null=False)
    state = models.CharField(max_length=2, default='', blank=True, null=False)
    campus_id = models.IntegerField(default='', blank=True, null=False)

    #create model manager
    object = models.Manager()
    #display the object output values in the form of a string
    def __str__(self):
        #returns the input value of the name and id
        #field as a tuple to display in the browser instead of default names
        display_name = '{0.campus_name}: {0.campus_id}'
        return display_name.format(self)
    #removes added 's' that django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = 'University Campus'