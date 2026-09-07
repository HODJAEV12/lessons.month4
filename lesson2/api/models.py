from django.db import models

class Books(models.Model):
    author = models.CharField(max_length=120, verbose_name="Автор книги")
    title = models.CharField(max_length=60, verbose_name="Название книги")
    description = models.TextField(blank=True, verbose_name="Описание книги", default="Без описания")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена книги")
    year = models.DateField(null=True, blank=True, verbose_name="Год реализации")
    image = models.ImageField(upload_to="book_image/", verbose_name="Изображение книги", null=True, blank=True)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

# ==============================================================================
# СПРАВОЧНИК: ВСЕ ВИДЫ ПОЛЕЙ В DJANGO MODELS (ШПАРГАЛКА)
# ==============================================================================
#
# 1. ТЕКСТОВЫЕ ПОЛЯ:
#    models.CharField(max_length=255)          - короткий текст, max_length обязателен
#    models.TextField(blank=True)              - длинный текст (описание, статья)
#    models.SlugField(unique=True)             - URL-метка (например: 'harry-potter')
#    models.EmailField()                       - строка с автоматической валидацией email
#    models.URLField()                         - строка с валидацией интернет-ссылки
#
# 2. ЧИСЛОВЫЕ ПОЛЯ:
#    models.IntegerField()                     - стандартное целое число
#    models.PositiveIntegerField()             - только положительное целое (страницы, возраст)
#    models.DecimalField(max_digits=10, decimal_places=2) - точные дробные числа (ЦЕНЫ, ДЕНЬГИ)
#        max_digits = максимальное количество цифр всего
#        decimal_places = символов после точки
#    models.FloatField()                       - дробные числа с плавающей точкой (рейтинг: 4.8)
#
# 3. ЛОГИЧЕСКИЕ:
#    models.BooleanField(default=True)         - True / False (да/нет, активен/неактивен)
#
# 4. ДАТА И ВРЕМЯ:
#    models.DateField()                        - только дата: 2026-09-03
#    models.DateTimeField(auto_now_add=True)   - дата и время создания (ставится 1 раз при создании)
#    models.DateTimeField(auto_now=True)       - дата и время обновления (обновляется при каждом .save())
#
# 5. ФАЙЛЫ И МЕДИА:
#    models.ImageField(upload_to='covers/')    - картинка (требует pip install Pillow)
#    models.FileField(upload_to='books_pdf/')  - любой файл (pdf, zip, docx)
#
# 6. СВЯЗИ (RELATIONS):
#    models.ForeignKey(OtherModel, on_delete=models.CASCADE) - связь "один ко многим"
#        on_delete=models.CASCADE  - удалили автора -> удалились все его книги
#        on_delete=models.SET_NULL - удалили автора -> поле автора у книги стало NULL
#        on_delete=models.PROTECT  - запретить удаление автора, пока есть его книги
#    models.ManyToManyField(OtherModel) - связь "многие ко многим" (книга - жанры)
#    models.OneToOneField(OtherModel, on_delete=models.CASCADE) - связь "один к одному"
#
# 7. ГЛАВНЫЕ ПАРАМЕТРЫ ПОЛЕЙ:
#    null=True        - разрешить значение NULL в базе данных
#    blank=True       - разрешить пустое значение в формах / сериализаторах
#    default=...      - значение по умолчанию (например, default=0 или default="Без названия")
#    unique=True      - уникальное значение во всей таблице БД
#    verbose_name=... - красивое название поля для админки
#    choices=...      - выбор из кортежей [('ru', 'Русский'), ('en', 'English')]