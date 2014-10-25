from django.contrib import admin

# Register your models here.
from .models import Join


class JoinAdmin(admin.ModelAdmin):
    list_display = ("email", "timestamp", 'updated')  #TODO: list_display doesnt display fields!
    class Meta:
        model = Join




admin.site.register(Join)