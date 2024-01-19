from django.contrib import admin

from .models import Post

admin.site.register

# admin.site.register(Post) / when the app was created, this was the original line
# an error happened when I add additional app called Heroes, reason why (Post) was removed
# in l5 to make the system work again.