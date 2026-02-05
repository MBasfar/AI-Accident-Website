from django.urls import path
from . import views
from .views import prediction_view
from .views import view_accident_details
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('previous_accident/', views.handle_previous_accident, name='previous_accident'),
    path('submit/', views.submit_accident, name='new_accident'),
    path('draw/', views.draw_accident, name='draw_accident'),
    path('predict/', prediction_view, name='predict-view'),
    path('accident/<str:accident_id>/', view_accident_details, name='view_accident_details'),
    path('submit-response/<str:accident_id>/', views.submit_response, name='submit_response'),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)