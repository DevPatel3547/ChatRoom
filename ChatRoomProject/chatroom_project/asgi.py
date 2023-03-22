import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chatroom_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatroom_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chatroom_app.routing.websocket_urlpatterns
        )
    ),
})
