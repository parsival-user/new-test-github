from django.db import models

# Create your models here.


STATUS = (
    ('yetkazib_berilgan','Yetkazib berilgan'),
    ('tayyorlanmoqda', 'Tayyorlanmoqda'),
)

PRODUCT = (
    ('hot_dog','Hot Dog'),
    ('lavash','Lavash'),
    ('pitsa','Pitsa'),
    ('burger','Burger'),
    ('donar','Donar'),
    ('sandvich','Sandvich'),
)

LOCATION = (
    ('andijon_tumani','Andijon tumani'),
    ('yangi_bozor','Yangi bozor'),
    ('eski_shahar','Eski shahar'),
    ("o'bekiston_ko'chasi","O'zbekiston ko'chasi"),
    ('bobur_kochasi','Bobur kochasi'),
    ("bog'ishamol","Bog'ishamol"),
    ("jarqugon","Jarqo'rg'on"),
)

class Dostavka(models.Model):
    """
    Dostavka uchun modellar
    """
    fullname = models.CharField( max_length=300)
    title = models.CharField(max_length=200,choices=PRODUCT,default=0)
    count = models.PositiveBigIntegerField(default=1, null=True, blank=True)
    price = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    all_price = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    location = models.CharField(max_length=200,choices=LOCATION,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS, default=0)




    class Meta:
        ordering = ['id']
        verbose_name = 'Dostavka'
        verbose_name_plural = 'Dostavka'


    def __str__(self):
        return f"{self.fullname} {self.title}"



    def product_price(self):
        return self.price * self.count

