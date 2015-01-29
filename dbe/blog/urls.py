from django.conf import urls
from blog.views import PostView, Main, ArchiveMonth

urlpatterns = patterns("",
   (r"^$"                            , Main.as_view(), {}, "main"),
   (r"^post/(?P<dpk>\d+)/$"          , PostView.as_view(), {}, "post"),
   (r"^archive_month/(\d+)/(\d+)/$"  , ArchiveMonth.as_view(), {}, "archive_month"),
)

