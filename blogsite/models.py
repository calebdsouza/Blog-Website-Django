# Version 0.0001
# Import required packages
from django.db import models
from django.utils import timezone

'''Represent a blog post object'''
class Post(models.Model): 
    # Get the author's ID for this Post
    author = models.ForeignKey('auth.User')
    # Get the title for this Post
    title = models.CharField(max_length=200)
    # Get the contents for this Post
    text = models.TextField()
    # Get the date that this Post was created
    created_date = models.DateTimeField(default=timezone.now)
    # Get the date that this Post was published
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        '''
        (Post) -> NoneType
        Set the published date for this Post object.
        REQ: Must be called upon a valid Post object
        '''        
        # Set the publishing date of this Post to the time of posting
        self.published_date = timezone.now()
        # Saves the information changed above
        self.save()

    def __str__(self):
        '''
        Return a String representation of the Post obejct, which this
        method is called upon. 
        REQ: Must be called upon a valid Post object
        '''
        # return the title as the string representation of this Post
        return self.title