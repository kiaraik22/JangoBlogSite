from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from slugify import slugify

# Create your models here.

# описание модели поста
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст поста")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания", editable=False) # editable (параметр который отвечает за возможность редактирования поля)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор",related_name="posts")
    image = models.ImageField(upload_to='posts/', null=True,blank=True, verbose_name='Изображение')
    slug = models.SlugField(max_length=200, unique=True, editable=False, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:read_post', kwargs={'slug':self.slug})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title