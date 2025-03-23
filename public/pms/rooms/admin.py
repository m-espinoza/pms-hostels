from django.contrib import admin
from .models import Room, Unit

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_type', 'base_price', 'capacity', 'is_active', 'created_at')
    list_filter = ('room_type', 'is_active')
    search_fields = ('name', 'description')
    date_hierarchy = 'created_at'
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'room_type', 'capacity', 'base_price', 'description', 'is_active')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_type', 'room',  'is_active', 'created_at')
    list_filter = ('unit_type', 'room', 'is_active')
    search_fields = ('name', 'room__name')
    date_hierarchy = 'created_at'
    ordering = ('room', 'name')
    fieldsets = (
        (None, {
            'fields': ('name', 'bed_type', 'room', 'is_active')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')