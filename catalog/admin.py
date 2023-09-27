from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Focus)
#admin.site.register(Director)
#admin.site.register(Actor)
admin.site.register(Status)
#admin.site.register(Status)
#admin.site.register(Kino)
admin.site.register(Country)
from django.contrib import admin

# Register your models here.
class Actoradmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'born')#столбик в панель админа
    list_display_links = ('fname', 'lname')#работает как сылка
admin.site.register(Actor,Actoradmin)#регистрирует модель актера

class Directoradmin(admin.ModelAdmin):
    list_display = ('fname', 'lname')
    list_display_links = ('fname', 'lname')
admin.site.register(Director,Directoradmin)

class Kinoadmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'director', 'display_actors')
    list_filter = ('status', 'ganre', 'rating')
    fieldsets = (('О фильме', {'fields': ('title', 'summary', 'actor')}),
                 ('Рейтинг', {'fields': ('rating', 'ager', ' status')}),
                 ('Остальное', {'fields': ('ganre', 'country', 'director', 'year')}))
admin.site.register(Kino,Kinoadmin)

class Stinline(admin.TabularInline):
    model = Kino

class Statusadmin(admin.ModelAdmin):
    inlines = [Stinline]
admin.site.register(Status, Statusadmin)
