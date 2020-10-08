from django.urls import path
from .views import (RamenAdd, RamenDelete, RamenDetail, RamenForm, RamenHome,
RamenList, RamenUpdate)

app_name = 'rating'

urlpatterns = [
    path('', RamenHome.as_view(), name='ramen_home'),
    path('list/', RamenList.as_view(), name='ramen_list'),
    path('<int:id>', RamenDetail.as_view(), name='ramen_detail'), 
    path('add/', RamenAdd.as_view(), name='ramen_add'),
    path('update/<int:id>', RamenUpdate.as_view(), name='ramen_update'),
    path('delete/<int:id>', RamenDelete.as_view(), name='ramen_delete'),
]