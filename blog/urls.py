from django.urls import path
from .views import (
    news_update_view,
    newslist_view,
    detail_list_view,
    news_create_view,
    task_delete_view,
)

urlpatterns = [
    path('news-update/<int:id>', news_update_view),
    path('news-list/', newslist_view),
    path('news-detail/<int:id>', detail_list_view),
    path('news-create/',news_create_view),
    path('news-delete/<int:id>', task_delete_view),
]
