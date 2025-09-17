from django.db import models

class Project(models.Model):
    TECHNOLOGY_CHOICES = [
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('JavaScript', 'JavaScript'),
        ('React', 'React'),
        ('Vue', 'Vue'),
        ('PostgreSQL', 'PostgreSQL'),
        ('Docker', 'Docker'),
        ('FastAPI', 'FastAPI'),
        ('SQLAlchemy', 'SQLAlchemy'),
        ('SQLite', 'SQLite'),
        ('python-telegram-bot', 'python-telegram-bot')    
    ]
    
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    technology = models.CharField(max_length=20, choices=TECHNOLOGY_CHOICES, verbose_name='Технология')
    image = models.ImageField(upload_to='project_images/', blank=True, verbose_name='Изображение')
    github_link = models.URLField(max_length=200, blank=True, verbose_name='Ссылка на GitHub')
    star_count = models.IntegerField(default=0, verbose_name='Звёзды на GitHub')
    fork_count = models.IntegerField(default=0, verbose_name='Форки на GitHub')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-created_on']

    def __str__(self):
        return self.title