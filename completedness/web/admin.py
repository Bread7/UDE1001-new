from django.contrib import admin
from db.models import users
# from db.models import pointsUser

# from pathlib import Path
# db = str(Path().absolute()) + '/db'
# from db import users

admin.site.register(users)
# admin.site.register(pointsUser)
# admin.site.register(users, pointsUser)