from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    guest_name = models.CharField(max_length=255)
    check_in = models.DateField()
    check_out = models.DateField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.guest_name} - {self.listing.title}"


class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=255)
    rating = models.IntegerField()
    comment = models.TextField()
    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer_name} - {self.rating}/5"
