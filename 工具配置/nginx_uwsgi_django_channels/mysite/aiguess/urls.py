from aiguess.views import SaveImage, GetUserCurImage, SavePlayImage, GetPlayImage, UserImgaeList,  GetOthersImage#,InsertImageId
from django.urls import path, re_path


urlpatterns = [
    path('userImageList', UserImgaeList.as_view()),
    path('saveImage', SaveImage.as_view()),
    path('getCurImage', GetUserCurImage.as_view()),
    path('savePlayImage', SavePlayImage.as_view()),
    path('getPlayImage', GetPlayImage.as_view()),
    # path('insertImageId$', InsertImageId.as_view()),
    path('getOthersImage', GetOthersImage.as_view()),
]
