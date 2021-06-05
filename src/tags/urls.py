from django.urls import path
from tags.views import TaggedItemListView, TaggedItemDetailView

urlpatterns = [
    path("", TaggedItemListView.as_view()),
    path("<slug:tag>", TaggedItemDetailView.as_view()),
]
