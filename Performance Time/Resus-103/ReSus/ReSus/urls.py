from django.urls import path
from Resus_App import views

urlpatterns = [
    path('', views.QueryCyper, name='QueryCyper'),
    path('run-cypher-query/', views.run_cypher_query, name='run_cypher_query'),
    # path('cv/', views.cv_jd_similarity_view, name='cv_jd_similarity'),
    # path('cv2/', views.cv_list_view, name='cv_list_view'),
]