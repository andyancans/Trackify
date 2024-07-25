from django.urls import path, include
from portfolio.views import my_profile, add_holdings, remove_holding
from portfolio.views import remove_holdings, remove_holding_by_id, remove_holding
from .views import home, register, login_view, user_logout, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', my_profile, name='my_profile'),
    path('add-holdings/', add_holdings, name='add_holdings'),
    path('remove-holding/<int:holding_id>/', remove_holding, name='remove_holding'),
    path('remove_holdings/', remove_holdings, name='remove_holdings'),
    path('remove_holding/<int:holding_id>/', remove_holding_by_id, name='remove_holding_by_id'),
]
