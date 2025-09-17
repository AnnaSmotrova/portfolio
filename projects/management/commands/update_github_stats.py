from django.core.management.base import BaseCommand
from projects.models import Project
import requests
from urllib.parse import urlparse

class Command(BaseCommand):
    help = 'Обновляет количество звезд и форков для проектов с указанной ссылкой на GitHub'

    def handle(self, *args, **options):
        projects = Project.objects.exclude(github_link='').filter(is_published=True)
        
        self.stdout.write(f'Начинаю обновление для {projects.count()} проектов...')
        
        for project in projects:
            try:
                path = urlparse(project.github_link).path
                parts = path.strip('/').split('/')
                
                if len(parts) >= 2:
                    owner, repo = parts[0], parts[1]
                    api_url = f'https://api.github.com/repos/{owner}/{repo}'

                    response = requests.get(api_url, timeout=10)
                    response.raise_for_status()
                    
                    data = response.json()
                    project.star_count = data['stargazers_count']
                    project.fork_count = data['forks_count']
                    project.save()

                    self.stdout.write(
                        self.style.SUCCESS(
                            f'✓ {project.title}: {project.star_count} звёзд, {project.fork_count} форков'
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f'✗ Некорректная ссылка GitHub для проекта: {project.title}'
                        )
                    )

            except requests.exceptions.RequestException as e:
                self.stdout.write(
                    self.style.ERROR(f'✗ Ошибка API для {project.title}: {e}')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'✗ Общая ошибка для {project.title}: {e}')
                )
        
        self.stdout.write(self.style.SUCCESS('Обновление завершено!'))