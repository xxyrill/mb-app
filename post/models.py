from django.contrib import admin

# need nmu ni iexecute para mag work ang admin.site.register(Post)

from django.db import models

# nag import si django ug models para maka create ka ug
# new database models. Need nmu mag create ug model para maka store ka ug
# text content sa message board post.
class Post(models.Model):
    text = models.TextField()

# diri nag create ka ug new db model called Post nga naay text field
# ug gi-specify nato nga kana nga field mag hold ug TextField().

    def __str__(self):
        return self.text[:50]

# dri nag define ka ug function, ang use ani kay gamiton as description ang
# content nga gi post up to 50 char. i check ang admin site para masabatan nmu.

admin.site.register(Post)

# dri na create ang Post app sa admin site
