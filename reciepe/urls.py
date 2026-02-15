from django.urls import path
from reciepe import views

urlpatterns = [
    path("", views.home, name='home'),
    path("view_rec/", views.view_rec, name='view_rec'),
    path("view_one/<str:id>/", views.view_one, name='view_one'),
    path("update_rec/<str:rec_id>/", views.update_rec, name='update_rec'),
    path("delete_rec/<str:rec_id>/", views.delete_rec, name='delete_rec'),
]