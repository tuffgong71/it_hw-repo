from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('zones/', views.ZoneListView.as_view(), name='zones'),
        path('zone/<int:pk>',views.ZoneDetailView.as_view(), name='zone-detail'),
        path('location/<int:pk>',views.LocationDetailView.as_view(), name='location-detail'),
        path('categories/', views.CategoryListView.as_view(), name='categories'),
        path('category/<int:pk>',views.CategoryDetailView.as_view(), name='category-detail'),
        path('equipment/<int:pk>', views.EquipmentDetailView.as_view(), name='equipment-detail'),
        path('equipment/<int:pk>/edit/', views.EquipmentEditView.as_view(), name='equipment-edit'),
]



#        path('equipment/<int:pk>/service/', views.EquipmentServiceView.as_view(), name='equipment-service'),




#        path('create/', views.EquipmentCreateView.as_view(), name='equipment-create'),
#        path('', views.EquipmentInfoView, name='base_equipment'),