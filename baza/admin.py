from django.contrib import admin
from .models import Klient, Lokalizacja, Moduly, Licencja


admin.site.register(Klient)
admin.site.register(Lokalizacja)
admin.site.register(Moduly)
admin.site.register(Licencja)
