from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Booking
from cars.models import Car
from django.utils.dateparse import parse_date
from datetime import date

@login_required
def book_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
        
        start_date = parse_date(start_date_str)
        end_date = parse_date(end_date_str)
        
        if not start_date or not end_date:
            messages.error(request, "Invalid dates.")
            return redirect('car_detail', pk=pk)
            
        if start_date < date.today():
             messages.error(request, "Cannot book in the past.")
             return redirect('car_detail', pk=pk)

        if end_date <= start_date:
            messages.error(request, "End date must be after start date.")
            return redirect('car_detail', pk=pk)
            
        # Check availability
        overlapping_bookings = Booking.objects.filter(
            car=car,
            start_date__lt=end_date,
            end_date__gt=start_date,
            status__in=['PENDING', 'CONFIRMED']
        )
        
        if overlapping_bookings.exists():
            messages.error(request, "Car is already booked for these dates.")
            return redirect('car_detail', pk=pk)
            
        # Calculate price
        days = (end_date - start_date).days
        total_price = days * car.price_per_day
        
        Booking.objects.create(
            user=request.user,
            car=car,
            start_date=start_date,
            end_date=end_date,
            total_price=total_price,
            status='PENDING'
        )
        
        messages.success(request, "Booking requested successfully!")
        return redirect('booking_history')
        
    return redirect('car_detail', pk=pk)

class BookingHistoryView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/booking_history.html'
    context_object_name = 'bookings'
    
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-created_at')

class MakePaymentView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'bookings/payment.html'
    context_object_name = 'booking'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user, status='PENDING')

    def post(self, request, *args, **kwargs):
        booking = self.get_object()
        # Mock payment processing
        booking.status = 'CONFIRMED'
        booking.is_paid = True
        booking.payment_date = timezone.now()
        booking.save()
        messages.success(request, "Payment successful! Booking confirmed.")
        return redirect('booking_receipt', pk=booking.pk)

class CancelBookingView(LoginRequiredMixin, View):
    def post(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk, user=request.user, status='PENDING')
        booking.status = 'CANCELLED'
        booking.save()
        messages.success(request, "Booking cancelled successfully.")
        return redirect('booking_history')

class BookingReceiptView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'bookings/receipt.html'
    context_object_name = 'booking'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user, status='CONFIRMED')
