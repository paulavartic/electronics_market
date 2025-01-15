from django.db import models
from django.contrib.auth.models import User

NULLABLE = {'blank': True, 'null': True}


class Supplier(models.Model):
    """Supplier model."""
    name = models.CharField(
        max_length=255,
        verbose_name='Supplier name',
        help_text='Enter the name of the supplier'
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name='Debt',
    )

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model."""
    name = models.CharField(
        max_length=255,
        verbose_name='Name',
    )
    model = models.CharField(
        max_length=255,
        verbose_name='Model',
        **NULLABLE,
    )
    photo = models.ImageField(
        upload_to='market/photo',
        verbose_name='Photo',
        help_text='Add a photo',
        **NULLABLE
    )
    release_date = models.DateField(
        verbose_name='Release date',
        **NULLABLE,
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class ChainUnit(models.Model):
    """Chain unit model."""
    LEVEL_CHOICES = [
        (0, 'Factory'),
        (1, 'Retail chain'),
        (2, 'Individual entrepreneur'),
    ]

    name = models.CharField(
        max_length=255,
        verbose_name='Name',
    )
    email = models.EmailField(
        verbose_name='Email',
    )
    country = models.CharField(
        max_length=100,
        verbose_name='Country',
    )
    city = models.CharField(
        max_length=100,
        verbose_name='City'
    )
    street = models.CharField(
        max_length=100,
        verbose_name='Street',
    )
    house_number = models.CharField(
        max_length=10,
        verbose_name='House number'
    )
    products = models.ManyToManyField(
        Product,
        related_name='chain_units',
        verbose_name='Products'
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        verbose_name='Supplier'
    )
    debt_to_supplier = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name='Debt to supplier'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creation time'
    )
    level = models.IntegerField(choices=LEVEL_CHOICES)

    class Meta:
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'

    def __str__(self):
        return self.name
