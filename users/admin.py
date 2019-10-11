from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
class CustomUserAdmin(UserAdmin):
# Inherited from UserAdmin to customize the default admin panel display
	model = CustomUser
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	list_display = ['email','username']
	fieldsets = UserAdmin.fieldsets + (
										 (None,
										 {'fields':('category','mob_num',)}
										 ),
									   )
	add_fieldsets = (

		(None,{
			'classes':('wide'),
			'fields':('email','username','password1','password2','is_staff','is_active')
			}),
					)

admin.site.register(CustomUser, CustomUserAdmin)