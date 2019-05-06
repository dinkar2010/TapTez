
from django.conf.urls import url
from django.contrib import admin
from taptez import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create_vendor/', views.createVendorProfile),
    url(r'^vendor_list/', views.VendorListView.as_view()),

]
