from django.contrib import admin

from mk_burger.core.models import Bread, Burger, Meat, Optional, Status


@admin.register(Bread)
class BreadAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tipo",
        "is_active",
        "created_at",
        "created_at",
    )

    list_filter = ("is_active",)

    search_fields = ("tipo",)

    readonly_fields = (
        "id",
        "created_at",
        "modified_at",
    )


@admin.register(Meat)
class MeatdAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tipo",
        "is_active",
        "created_at",
        "created_at",
    )

    list_filter = ("is_active",)

    search_fields = ("tipo",)

    readonly_fields = (
        "id",
        "created_at",
        "modified_at",
    )


@admin.register(Optional)
class OptionalAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tipo",
        "is_active",
        "created_at",
        "created_at",
    )

    list_filter = ("is_active",)

    search_fields = ("tipo",)

    readonly_fields = (
        "id",
        "created_at",
        "modified_at",
    )


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tipo",
        "is_active",
        "created_at",
        "created_at",
    )

    list_filter = ("is_active",)

    search_fields = ("tipo",)

    readonly_fields = (
        "id",
        "created_at",
        "modified_at",
    )


@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "carne",
        "pao",
        "status",
        "is_active",
        "created_at",
        "created_at",
    )

    list_filter = (
        "is_active",
        "status",
    )

    search_fields = ("nome",)

    readonly_fields = (
        "id",
        "created_at",
        "modified_at",
    )
