from django.urls import path

from . import views

urlpatterns = [

    path('add', views.add_list),
    path('tolist', views.to_list),
    path('update', views.update_list),
    path('done', views.done_list),
    path('delete', views.delete_list)

]
