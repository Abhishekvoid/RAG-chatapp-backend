"""
ASGI config for RAG project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import chat.routing 


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RAG.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),                 # http = normal Django
    "websocket": AuthMiddlewareStack(               # websocket = channels 
        
            URLRouter(chat.routing.websocket_urlpatterns)
    ),
})