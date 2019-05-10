from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.

class Category(models.Model):

    asset_cat = models.CharField(
            max_length=20,
            unique=True,
            verbose_name='asset category')

    def __str__(self):
        return "{}".format(self.asset_cat)

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural='categories'

class Zone(models.Model):

    zone_loc = models.CharField(
            max_length=20,
            unique=True,)

    def __str__(self):
        return "{}".format(self.zone_loc)

    def get_absolute_url(self):
        return reverse('zone-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural='zones'

class Location(models.Model):

    asset_loc = models.CharField(
            max_length=20,
            unique=True,
            default='storage',
            verbose_name='asset location')

    zone_loc = models.ForeignKey('zone', default=None, on_delete=models.PROTECT, verbose_name='zone')

    dept = models.ForeignKey('department',on_delete=models.PROTECT)

    def __str__(self):
        return self.asset_loc

    def get_absolute_url(self):
        return reverse('location-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = 'locations'
        ordering = ["asset_loc"]


class Department(models.Model):

    dept = models.CharField(
            max_length=20,
            unique=True,
            verbose_name='department')

    def __str__(self):
        return self.dept

    def get_absolute_url(self):
        return reverse('departmen-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = 'departments'


class Status(models.Model):
    state = models.CharField(
            max_length=15,
            unique=True,
            default='stored',
            verbose_name='status')

    def __str__(self):
        return self.state

    def get_absolute_url(self):
        return reverse('status-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = 'status'


class Equipment(models.Model):

    name = models.CharField(
            max_length=15,
            unique=True,
            verbose_name='asset name')
    asset_cat = models.ForeignKey('category',on_delete=models.PROTECT,verbose_name='asset category')
    asset_loc = models.ForeignKey('location',on_delete=models.PROTECT,verbose_name='asset location')
    state = models.ForeignKey('status',on_delete=models.PROTECT,verbose_name='status')

    brand = models.CharField(
            max_length=15,
            unique=False,
            blank=True)

    model = models.CharField(
            max_length=12,
            unique=False,
            blank=True,
            verbose_name='model number')

    service_tag = models.CharField(
            max_length=15,
            unique=False,
            blank=True,
            verbose_name='service tag')

    DHCP = 'DHCP'
    STATIC = 'STATIC'
    NA = 'N/A'
    IP_CONFIG_CHOICES = (
            (DHCP, 'DHCP'),
            (STATIC, 'STATIC'),
            (NA, 'N/A'),
    )

    ip_config = models.CharField(
            max_length=6,
            choices=IP_CONFIG_CHOICES,
            default=NA,
            verbose_name='ip configuration')

    ip_address = models.GenericIPAddressField(
            protocol='both',
            blank=True,
            null=True,
            verbose_name='ip address')

    serial = models.CharField(
            max_length=40,
            unique=False,
            blank=True,
            verbose_name='serial number')

    os = models.CharField(
            max_length=15,
            unique=False,
            blank=True,
            verbose_name='operating system')

    ram = models.CharField(
            max_length=12,
            unique=False,
            blank=True)

    hd = models.CharField(
            max_length=20,
            unique=False,
            blank=True,
            verbose_name='hard drive')

    pro = models.CharField(
            max_length=40,
            unique=False,
            blank=True,
            verbose_name='processor')

    bios = models.CharField(
            max_length=10,
            unique=False,
            blank=True,
            verbose_name='bios version')

    firm = models.CharField(
            max_length=20,
            unique=False,
            blank=True,
            verbose_name='firmware version')

    ports = models.IntegerField(
            blank=True,
            null=True,
            default=None,
            verbose_name='number of ports')

    ext = models.IntegerField(
            blank=True,
            null=True,
            default=None,
            verbose_name='phone extension')

    p_date = models.DateField(
            auto_now=False,
            auto_now_add=False,
            null=True,
            blank=True,
            default=None,
            verbose_name='purchase date')

    d_date = models.DateField(
            auto_now=False,
            auto_now_add=False,
            null=True,
            blank=True,
            default=None,
            verbose_name='deployment date')

    i_date = models.DateField(
            auto_now=False,
            auto_now_add=False,
            null=True,
            blank=True,
            default=None,
            verbose_name='image date')

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse('equipment-detail', args=[str(self.id)])

    class Meta:
        ordering = ['asset_cat', 'name']
        verbose_name_plural = 'pieces of equipment'


class Action(models.Model):
    name = models.ForeignKey('equipment',on_delete=models.PROTECT,verbose_name='asset name',blank=False)

    dt = models.DateTimeField(
            auto_now_add=True,
            verbose_name='date and time of incident')

    incident = models.TextField(
            blank=True,
            null=True)

    CHANGE = 'CHANGE'
    SERVICE = 'SERVICE'
    ACTION_CHOICES = (
            (CHANGE, 'CHANGE'),
            (SERVICE, 'SERVICE')
    )

    act = models.TextField(
            blank=True,
            choices=ACTION_CHOICES,
            null=True,
            verbose_name='action taken')

    act_detail = models.TextField(
            verbose_name='action detail',
            blank=False)

    result = models.TextField(
            blank=True,
            null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-dt']
        verbose_name_plural = 'service calls'
