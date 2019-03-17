from django.db import models


class User(models.Model):
    '''
    profile
    name
    contacts
    projects
    rating
    '''
    type = models.TextField()


class Rating(models.Model):
    pass


class UserProfile(models.Model):
    '''
    Name
    Contacts
    Description (education, skills, etc.)
    Working/Volunteering/Ownership of projects (history, current)
    Rating
    Photo
    Comments
    Subscriptions
    '''


class Admin(models.Model):
    pass


class Startup(models.Model):
    pass


class Project(models.Model):
    '''
    Event_name = models.TextField()
    Owner =
    Description =
    Requirements =
    Contacts =
    Rating =
    Reward =
    Photo =
    Comments =
    '''
