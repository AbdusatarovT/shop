"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from applications.account.views import ActivationView


schema_view = get_schema_view(
    openapi.Info(
        title='Python 21 shop',
        default_version='v1',
        description='Наш первый интернет магазин'

    ),
    public=True

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger')),
    path('api/v1/account/', include('applications.account.urls')),
    path('api/v1/product/', include('applications.product.urls')),
    path('api/v1/order/', include('applications.cart.urls')),
    path('api/v1/contact/', include('applications.spam.urls')),
    #

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # для отображения картинок


