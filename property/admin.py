from django.contrib import admin

from .models import Flat, Complaint



class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'owners_phonenumber',
        'owner_pure_phone',
        )
    list_editable = ('new_building',)
    list_filter = (
        'new_building',
        'rooms_number',
        'has_balcony',
        'active',
        )
    raw_id_fields = (
        'liked_by',
        )

admin.site.register(Flat, FlatAdmin)

class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'complaint_flat',
        'complaint_text',
        )
    raw_id_fields = (
        'author',
        'complaint_flat',
        )


admin.site.register(Complaint, ComplaintAdmin)