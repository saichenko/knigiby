from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from apps.secondary_objects.models.for_books import Author, Genre, BookSeries, Publisher
from apps.users.models.profiles import Profile


class Product(models.Model):
    AGE_RESTRICTION_CHOICES = (
        (0, '0+'),
        (6, '6+'),
        (12, '12+'),
        (16, '16+'),
        (18, '18+'),
    )

    name = models.CharField('Название', max_length=90)
    authors = models.ManyToManyField(Author, verbose_name='Авторы')
    main_img = models.ImageField('Главное изображение', upload_to='main_product_images')
    usd_price = models.PositiveSmallIntegerField('Цена, $')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры', related_name='books')
    book_series = models.ForeignKey(BookSeries, verbose_name='Серия', on_delete=models.CASCADE, related_name='book')
    publisher = models.ForeignKey(Publisher, verbose_name='Издательство', on_delete=models.CASCADE, related_name='books')
    published = models.DateField('Опубликована')
    pages_number = models.PositiveSmallIntegerField('Кол-во страниц')
    cover = models.CharField('Переплёт', max_length=35)
    format = models.CharField('Формат', max_length=25)
    isbn = models.CharField('ISBN', max_length=19)
    weight_gr = models.PositiveSmallIntegerField('Вес, г')
    age_restriction = models.PositiveSmallIntegerField('Возрастное ограничение', choices=AGE_RESTRICTION_CHOICES)
    books_available = models.PositiveSmallIntegerField('Книг в наличии')
    rating = models.PositiveSmallIntegerField('Рейтинг', null=True, blank=True)
    created = models.DateTimeField('Создано', auto_now_add=True)
    last_modified = models.DateTimeField('Последнее изменение', auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name}'


class ProductComment(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE, related_name='product_comment')
    profile = models.ForeignKey(Profile, verbose_name='Профиль', on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    text = models.TextField('Текст')
    created = models.DateTimeField('Создано', auto_now_add=True)
    last_modified = models.DateTimeField('Последнее изменение', auto_now=True)

    class Meta:
        verbose_name = 'Комментарий к товару'
        verbose_name_plural = 'Коментарии к товарам'

    def __str__(self):
        return f'Комментарий под {self.product} от {self.profile.user.username}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE, related_name='image')
    image = models.ImageField('Изображение', upload_to='product_images')

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'

    def __str__(self):
        return f'{self.product.name} изображение'
