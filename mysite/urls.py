
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('virtual_cemetery/', include("vc.urls")),
    # path('wiki/', include("encyclopedia.urls")),
]
