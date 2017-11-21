from django.contrib import admin

# Register your models here.
from models import User, Fruit, Donut, Group


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)


class FruitAdmin(admin.ModelAdmin):
    pass


admin.site.register(Fruit, FruitAdmin)


class DonutAdmin(admin.ModelAdmin):
    pass


admin.site.register(Donut, DonutAdmin)


class GroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(Group, GroupAdmin)
