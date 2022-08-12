from django.urls import include, path
from rest_framework.routers import SimpleRouter

from cats.views import CatDetail, CatList, CatViewSet

urlpatterns = [
   path('cats/', CatList.as_view()),
   path('cats/<int:pk>', CatDetail.as_view()),
   ]

router = SimpleRouter()
router.register('cats', CatViewSet)

urlpatterns =  [path('', include(router.urls)),
]
