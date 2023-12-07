from django.urls import path, include
from hardathon.router import hardatons_router, detail_project_router, projects_router, partners_router


app_name = 'hardathon'
urlpatterns = [
    path('hardaton/', include(hardatons_router.urls)),
    path('project/', include(detail_project_router.urls)),
    path('projects/', include(projects_router.urls)),
    path('get_event_partners/', include(partners_router.urls)),
]
