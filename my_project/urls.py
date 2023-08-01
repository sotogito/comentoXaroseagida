from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mysite/', include('mysite.urls')),
    path('',include('pages.urls')),
    path('',include('account.urls')),
    #하위페이지를 적으면 DjangoApiUrl이 안된다...
    path('',include('mymail.urls')),
    path('',include('products.urls'))
]
