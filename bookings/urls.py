from django.urls import path
from .views import book_car, BookingHistoryView, MakePaymentView, CancelBookingView, BookingReceiptView

urlpatterns = [
    path('book/<int:pk>/', book_car, name='book_car'),
    path('my-bookings/', BookingHistoryView.as_view(), name='booking_history'),
    path('payment/<int:pk>/', MakePaymentView.as_view(), name='make_payment'),
    path('cancel/<int:pk>/', CancelBookingView.as_view(), name='cancel_booking'),
    path('receipt/<int:pk>/', BookingReceiptView.as_view(), name='booking_receipt'),
]
