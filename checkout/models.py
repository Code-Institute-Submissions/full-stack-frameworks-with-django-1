from django.db import models
from django.contrib.auth.models import User
from tickets.models import Ticket


class Order(models.Model):
    """
        Create the Order Model
        that creates the order table
        in the MySQL Database.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '#{0} - {1} - {2}'.format(self.id, self.order_date, self.user.username)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return '{0} - {1} - £{2}'.format(self.quantity, self.ticket.title, self.ticket.upvote_price)
