import requests
from django.core.management.base import BaseCommand
from account.models import User
from forum.models import Post

class Command(BaseCommand):
    help = 'Import JSON data from the given URLs and save to the database'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, help='Number of users to import', default=10)
        parser.add_argument('--posts', type=int, help='Number of posts to import', default=10)

    def handle(self, *args, **options):
        user_limit = options['users']
        post_limit = options['posts']
        
        self.import_users(user_limit)
        self.import_posts(post_limit)

    def import_users(self, limit):
        url = f'https://jsonplaceholder.typicode.com/users'
        response = requests.get(url)
        users = response.json()[:limit]
        
        imported_count = 0
        for user in users:
            if not User.objects.filter(id=user['id']).exists():
                User.objects.create(
                    id=user['id'],
                    name=user['name'],
                    username=user['username'],
                    email=user['email']
                )
                imported_count += 1
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {imported_count} users'))

    def import_posts(self, limit):
        url = f'https://jsonplaceholder.typicode.com/posts'
        response = requests.get(url)
        posts = response.json()[:limit]
        
        imported_count = 0
        for post in posts:
            if not Post.objects.filter(id=post['id']).exists():
                Post.objects.create(
                    id=post['id'],
                    userId_id=post['userId'],
                    title=post['title'],
                    body=post['body']
                )
                imported_count += 1
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {imported_count} posts'))
    