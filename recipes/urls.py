from django.urls import path

from recipes.views import home, contato, sobre
# Importe as funções da Views

urlpatterns = [
    path('', home),  # Home
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato),  # /contato/
]
