from django.contrib import admin

from .models import Flat, Complaint, Owner

class FlatInstanceInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ('created_at',)
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
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
    inlines = [FlatInstanceInline]

admin.site.register(Flat, FlatAdmin)

class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'flat',
        'text',
        )
    raw_id_fields = (
        'author',
        'flat',
        )


admin.site.register(Complaint, ComplaintAdmin)

class OwnerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phonenumber',
        'pure_phone',
        )
    raw_id_fields = (
        'flats',
        )


admin.site.register(Owner, OwnerAdmin)