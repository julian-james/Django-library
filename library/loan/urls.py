from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='loan-index'), # route for /loan/
    path('about/', views.about, name='loan-about'), # route for /loan/about
    # path('<id>/', views.show, name='loan-show'), # route for /loan/:id
    # path('<int:id>/', views.show, name='loan-show') # to accept only numbers as id param
    path('books/new/', views.create, name='book-create'),
    path('books/<int:book_id>/', views.show, name='book-show'),
    
]