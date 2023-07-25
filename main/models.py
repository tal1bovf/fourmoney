# from datetime import date
# from .tasks import send_email
# from django.core.exceptions import ValidationError
# from django.db import models
# from django.contrib.auth.models import User
# from django.utils.translation import gettext_lazy as _
#
#
# class Product(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     image = models.ImageField()
#     name = models.CharField(max_length=100)
#     category = models.CharField(max_length=100)
#     firm = models.CharField(max_length=100)
#     model_product = models.CharField(max_length=100)
#     color_product = models.CharField(max_length=100)
#     country_manufacture = models.CharField(max_length=100)
#     price = models.IntegerField()
#     treaty = models.BooleanField()
#
#     def __str__(self):
#         return self.name
#
#
# class Phone(models.Model):
#     name_model = models.TextField()
#     image = models.ImageField()
#     description = models.TextField()
#     price = models.IntegerField()
#     treaty = models.BooleanField()
#     phone = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name_model
#
#
# class Tv(models.Model):
#     name_model = models.CharField(max_length=100)
#     image = models.ImageField()
#     description = models.TextField()
#     price = models.IntegerField()
#     email = models.EmailField()
#     characteristics = models.TextField()
#     tv = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name_model
#
#
# class Noutbook(models.Model):
#     name_model = models.CharField(max_length=100)
#     image = models.ImageField()
#     description = models.TextField()
#     price = models.IntegerField()
#     email = models.EmailField()
#     characteristics = models.TextField()
#     memory = models.IntegerField()
#     Noutbook = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name_model
#
#
# class Tablet(models.Model):
#     name_model = models.CharField(max_length=100)
#     image = models.ImageField()
#     description = models.TextField()
#     price = models.IntegerField()
#     email = models.EmailField()
#     characteristics = models.TextField()
#     memory = models.IntegerField()
#     tablet = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name_model
#
#
# class Company(models.Model):
#     Store_type = (
#         (1, _('Market')),
#         (2, _('Branch')),
#         (3, _('Point of sale'))
#     )
#     Store_type = models.IntegerField(choices=Store_type)
#     phone_number = models.IntegerField()
#     address = models.CharField(max_length=50)
#     bank_account_number = models.IntegerField()
#     bank_number = models.IntegerField()
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     admin1 = models.ForeignKey(User, blank=True, null=True)
#     admin2 = models.ForeignKey(User, blank=True, null=True)
#     admin3 = models.ForeignKey(User, blank=True, null=True)
#     admin4 = models.ForeignKey(User, blank=True, null=True)
#     admin5 = models.ForeignKey(User, blank=True, null=True)
#
#     def __str__(self):
#         return self.Store_type
#
#
# class TreatyCompany(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     dont_like = models.BooleanField(default=True)
#     exchange = models.IntegerField(default=5, blank=True, null=True)
#     if_bad = models.BooleanField(default=True)
#     ex_change = models.IntegerField(default=5, blank=True, null=True)
#     lowered_price_product = models.BooleanField(default=True)
#     lowered_price_product_per = models.IntegerField(default=5)
#
#
# class Credit(models.Model):
#     product_id = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
#     month = models.IntegerField(default=12)
#     date = models.DateField(auto_now=True)
#     quantity = models.IntegerField
#
#     @property
#     def price(self):
#         return Product.objects.filter(credit_id=self.id)
#     first_payment = models.BooleanField(default=True)
#     first_payment_amount = models.IntegerField(null=True, blank=True)
#
#     def send_email_notification(self):
#         if self.date == date.today():
#             total_sum = sum([choose.quantity * choose.product.price for choose in Chooses.objects.all()])
#             if total_sum == self.price:
#                 message = f'Payment completed. No further payment required.'
#             elif self.price < total_sum:
#                 message = f'Please make a payment. You need to pay an additional amount of {total_sum - self.payment}. Check our website.'
#             else:
#                 return
#
#             send_email.delay('roncrist5575@gmail.com', message)

from django.db import models
from django.contrib.auth.models import User


class Merchant(models.Model):
    type_merchant = models.CharField(max_length=100)
    name_shop = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    addres = models.TextField()
    name_bank = models.CharField(max_length=100)
    mfo = models.IntegerField()
    bank_number = models.IntegerField()

    def __str__(self):
        return self.type_merchant


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    firm = models.CharField(max_length=100)
    model_product = models.CharField(max_length=100)
    ikpu_product = models.CharField(max_length=100)
    color_product = models.CharField(max_length=100)
    country_manufacture = models.CharField(max_length=100)
    price = models.IntegerField()

    # phone = models.ForeignKey(Phone, null=True, blank=True, on_delete=models.CASCADE)
    # laptop = models.ForeignKey(Komp, null=True, blank=True, on_delete=models.CASCADE)
    # telev = models.ForeignKey(Telev, null=True, blank=True, on_delete=models.CASCADE)
    # plan = models.ForeignKey(Plan, null=True, blank=True, on_delete=models.CASCADE)
    #
    # def clean(self):
    #     filled_fields = 0
    #
    #     if self.phone is not None:
    #         filled_fields += 1
    #
    #     if self.laptop is not None:
    #         filled_fields += 1
    #
    #     if self.telev is not None:
    #         filled_fields += 1
    #
    #     if self.plan is not None:
    #         filled_fields += 1
    #
    #     if filled_fields > 1:
    #         raise ValidationError("Only one field (phone, laptop, telev, plan) can be filled.")

    def __str__(self):
        return self.name


class Phone(models.Model):
    name_model = models.TextField()
    image = models.ImageField()
    description = models.TextField()
    price = models.IntegerField()
    dogovor = models.BooleanField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    characteristics = models.TextField()
    phone = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_model


class Telev(models.Model):
    name_model = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    price = models.IntegerField()
    dogovor = models.BooleanField()
    email = models.EmailField()
    characteristics = models.TextField()
    telev = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_model


class Komp(models.Model):
    name_model = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    price = models.IntegerField()
    dogovor = models.BooleanField()
    email = models.EmailField()
    characteristics = models.TextField()
    memory = models.IntegerField()
    komp = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_model


class Plan(models.Model):
    name_model = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    price = models.IntegerField()
    dogovor = models.BooleanField()
    email = models.EmailField()
    characteristics = models.TextField()
    memory = models.IntegerField()
    plan = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_model


class ShoppingCard(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Shopping Card'
        verbose_name_plural = 'Shopping Cards'

    def __str__(self):
        return self.product.name


class Order(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    rassrochka = models.DateTimeField(auto_now_add=True)
    every_pays = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    own_partifition = models.IntegerField()
    installment_balance = models.IntegerField()
    status = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    number_cart = models.IntegerField()
    valid_about = models.IntegerField()

    def __str__(self):
        return self.name


class Users(models.Model):
    phone_number = models.IntegerField()
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.TextField()

    def __str__(self):
        return self.name


class Client(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    pnfl = models.IntegerField()
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport_number = models.IntegerField()
    issued = models.CharField(max_length=100)
    date_give = models.DateTimeField(auto_now_add=True)
    goden_about = models.DateTimeField(auto_now_add=True)
    nationality = models.CharField(max_length=100)
    citizienship = models.CharField(max_length=100)
    whos_addres = models.CharField(max_length=100)
    whos_number = models.CharField(max_length=100)
    number_card = models.IntegerField()
    term_card = models.IntegerField()

    def __str__(self):
        return self.name


class Credit(models.Model):
    pnfl = models.IntegerField()
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport_number = models.IntegerField()
    issued = models.CharField(max_length=100)
    date_issue = models.DateTimeField()
    goden = models.IntegerField()
    nation = models.CharField(max_length=100)
    citizienship = models.CharField(max_length=100)
    whos_addres = models.CharField(max_length=100)
    addres = models.TextField()
    whos_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    card_number = models.IntegerField()
    card_term = models.IntegerField()

    def __str__(self):
        return self.name


class Chooses(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # quantity = models.IntegerField(default=1)
    quantity = models.BigIntegerField()
    credit = models.ForeignKey(Credit, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


# class Buys(models.Model):
#     Credit_Choices = (
#         (3, 3),
#         (4, 4),
#         (6, 6),
#     )
#     category = models.CharField(max_length=100, choices=Credit_Choices)
#     date = models.DateTimeField()
#     payment = models.FloatField()
#     chooses = models.ForeignKey(Chooses, on_delete=models.CASCADE)
#     credit = models.ForeignKey(Credit, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.category
#
#     @classmethod
#     def calculate_sum(cls):
#         return sum(cls.objects.values_list('payment', flat=True))

from datetime import date
from django.db import models
from .tasks import send_email


class Buys(models.Model):
    Credit_Choices = (
        (3, 3),
        (4, 4),
        (6, 6),
    )
    category = models.CharField(max_length=100, choices=Credit_Choices)
    date = models.DateTimeField()
    payment = models.FloatField()
    chooses = models.ForeignKey(Chooses, on_delete=models.CASCADE)
    credit = models.ForeignKey(Credit, on_delete=models.CASCADE)

    def __str__(self):
        return self.category

    def send_email_notification(self):
        if self.date.date() == date.today():
            total_sum = sum([choose.quantity * choose.product.price for choose in Chooses.objects.all()])
            if total_sum == self.payment:
                message = f'Payment completed. No further payment required.'
            elif self.payment < total_sum:
                message = f'Please make a payment. You need to pay an additional amount of {total_sum - self.payment}. Check our website.'
            else:
                return

            send_email.delay('roncrist5575@gmail.com', message)

