
from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter() #The default router extends the SimpleRouter, but also adds in a default API root view, and adds format suffix patterns to the URLs.
router.register('article', ArticleViewset, basename='article')
#router.register(prefix, Viewset Name, basename=...)

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    path('article/', article_list),
    path('detail/<int:pk>/',article_detail),
    
    path('article_class/', ArticleAPIView.as_view()),
    path('detail_class/<int:id>/', ArticleDetails.as_view()),
    path('generic_article/<int:id>/', GenericAPIView.as_view())
]