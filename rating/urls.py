from django.urls import path
from .views import (RamenHome, RamenAdd, RamenList, RamenDetail,
                     RamenUpdate, RamenDelete)

app_name = 'rating'

urlpatterns = [
    path('', RamenHome.as_view(), name='ramen'),
    path('add/', RamenAdd.as_view(), name='ramen_add'),
    path('list/', RamenList.as_view(), name='ramen_add'),
    path('<int:id>', RamenDetail.as_view(), name='ramen_detail'),
    path('update/<int:id>', RamenUpdate.as_view(), name='ramen_update'),
    path('delete/<int:id>', RamenDelete.as_view(), name='ramen_delete'),


]
    