from django.contrib import admin

from .models import Conversation, ConversationalMessage
# Register your models here.


admin.site.register(Conversation)
admin.site.register(ConversationalMessage)

