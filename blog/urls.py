from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, BlogCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_view/<int:pk>', BlogDetailView.as_view(), name='blog_view'),
    path('blog_update/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
