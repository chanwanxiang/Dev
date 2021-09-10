from django.conf.urls import url
from payment.views import order

urlpatterns = [
    url(r'^order/$',order)
]
