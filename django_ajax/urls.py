
"参考URL"
"DjangoでAjax（汎用クラスビューを使用）"
"https://qiita.com/skokado/items/a25d64cafa3db791b283"




"""django_ajax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from greeting import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/', views.GreetView.as_view(), name='greet'),
]