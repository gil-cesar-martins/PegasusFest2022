from django.urls import path

from .views import IndexView, PortfolioDetails1View, PortfolioDetails2View, PortfolioDetails3View 

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('portfolio-details1/', PortfolioDetails1View.as_view(), name='portfolio-details1'), #ano 2017
    path('portfolio-details2/', PortfolioDetails2View.as_view(), name='portfolio-details2'), #ano 2018
    path('portfolio-details3/', PortfolioDetails3View.as_view(), name='portfolio-details3'), #ano 2019
]