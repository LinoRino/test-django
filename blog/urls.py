from django.urls import path
# blog ディレクトリの中の views.py を import
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail', views.detail, name='detail'),
    path("register", views.AccountCreateView.as_view(), name="register"),
    path("login", views.AccountLoginView.as_view(), name="login"),
    path("mypage",views.MypageView.as_view(), name="mypage"),
    path("logout", views.AccountLogoutView.as_view(), name="logout"),
    path("mypage/new-article", views.ArticleCreateView.as_view(), name="mypage-new-article"),
    path("mypage/articles", views.MypageArticleView.as_view(), name="mypage-articles"),
    path("articles", views.ArticleListView.as_view(), name="articles"),
    path("articles/<id>", views.ArticleView.as_view(), name="article"),
    path("api/articles", views.ArticleApiView.as_view(), name="api"),
    path("api/articles/<article_id>", views.ArticleDetailView.as_view(), name="apu-articles-detail"),
    path("api/articles/<article_id>/comments", views.CommentApiClient.as_view(), name="api-articles-comments"),
    path("article-file", views.open_article_file, name="article-file")
]