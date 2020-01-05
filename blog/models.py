from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField()
    body = models.TextField()    
    image = models.ImageField(upload_to = 'images/') 

    #Add the Blog app to the settings
    # Create a migration
    #python manage.py makemigrations
    # Migrate
    #python manage.py migrate
    # Add to the admin 

    def summary(self):
        return self.body[:100]
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    def __str__(self):
        return self.title
