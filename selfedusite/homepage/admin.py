from django.contrib import admin
from homepage.models import Car, Category


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'brief_info')
    list_display_links = ('id', 'title')
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']

    @admin.display(description="Краткое описание")
    def brief_info(self, car:Car):
        return f"Описание: {len(car.content)} символов"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
#admin.site.register(Car, CarAdmin)

# Register your models here.
