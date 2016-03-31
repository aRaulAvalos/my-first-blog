from django.contrib import admin
from .models import Post

#registra nuestro objeto post en el administrador
#de Django para poder consultar o actualizar información del o de los post

admin.site.register(Post)

