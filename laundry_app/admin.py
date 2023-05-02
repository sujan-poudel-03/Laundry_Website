from django.contrib import admin
from laundry_app.models import Catogary_name, Item_detail
from laundry_app.models import *
from laundry_app.models import User     #   astrick sign refers all

admin.site.site_header = ' Laundry Admin '

# Register your models here.

admin.site.register(Catogary_name),
admin.site.register(Item_detail),
admin.site.register(Branch),
admin.site.register(ClientDetail),




# Learn Section

admin.site.register(person),
admin.site.register(registeration),
admin.site.register(UserProfileInfo),
admin.site.register(CRUD),
