from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("EXTRA"), {"fields": ("status",)}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

admin.site.register(Player)
admin.site.register(Club)
admin.site.register(Card)
admin.site.register(Turnir)
admin.site.register(Match)
admin.site.register(Trending)
admin.site.register(Sponsor)
admin.site.register(Product)
admin.site.register(SocialMedia)
# Register your models here.
