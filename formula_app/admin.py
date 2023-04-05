from csv import list_dialects
from django.contrib import admin
from .models import Input, Output

class InputAdmin(admin.ModelAdmin):
    list_display = ('alpha', 'betha', 'phi', 'delta_a', 'delta_p')

class OutputAdmin(admin.ModelAdmin):
    list_display = ('kag', 'kagh', 'kagv', 'kaph', 'teta_a', 'k0n', 'k0t', 'k0h', 'k0V', 'kpgh', 'kpph', 'kpch', 'teta_p')

admin.site.register(Input, InputAdmin)
admin.site.register(Output, OutputAdmin)