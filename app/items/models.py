from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    '''Категории товаров'''

    name = models.CharField('Категория', max_length=12)
    url = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    '''Подкатегории'''

    name = models.CharField('Подкатегория', max_length=20)
    url = models.SlugField(max_length=30, unique=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


GB_CHOICE = [
    ('64', '64 Gb'),
    ('128', '128 Gb'),
    ('256', '256 Gb'),
    ('512', '512 Gb'),
    ('1', '1 Tb'),

]
GRAY = 'GRAY'
BLACK = 'BLACK'
WHITE = 'WHITE'
BLUE = 'BLUE'
PINK = 'PINK'
COLOR_CHOICE = [
    (GRAY, 'Серый'),
    (BLACK, 'Черный'),
    (WHITE, 'Белый'),
    (BLUE, 'Голубой'),
    (PINK, 'Розовый'),

]

DISCOUNT_CHOICE = [
    (0, '0%'),
    (5, '5%'),
    (10, '10%'),
    (15, '15%'),
    (20, '20%'),
]


class Item(models.Model):
    """
    Товар
    """

    subcategory = models.ForeignKey(SubCategory, verbose_name='Подкатегория', on_delete=models.PROTECT)
    gb = models.CharField('Размер памяти', choices=GB_CHOICE, default='128', max_length=3)
    color = models.CharField('Цвет', choices=COLOR_CHOICE, max_length=7, default=BLACK)
    name = models.CharField('Название', max_length=40)
    description = models.TextField('Описание', blank=True, default='')
    price = models.PositiveIntegerField('Цена', default=0, help_text='В рублях')
    amount = models.PositiveIntegerField('Количество', default=0)
    slug = models.SlugField(max_length=55,default='' ,blank=True)
    image = models.ImageField('Изображение', upload_to='images')
    discount = models.PositiveIntegerField('Скидка' ,choices=DISCOUNT_CHOICE, null=True)
    new_price = models.IntegerField('Цена со скидкой', default=0, help_text='В рублях')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-price']

    def save(self, *args, **kwargs):
        self.new_price = ((100-int(self.discount))*int(self.price))//100
        self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField('Изображение', upload_to='news', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
