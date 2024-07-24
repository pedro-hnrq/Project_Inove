import requests
from django.core.management.base import BaseCommand
from account.models import User
from forum.models import Post
from information.models import Geo, Address, Company

class Command(BaseCommand):
    help = 'Import JSON data from JSONPlaceholder and save to the database'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, help='Number of users to import', default=10)

    def handle(self, *args, **options):
        user_limit = options['users']
        
        user_imported_count, post_imported_count = self.import_data(user_limit)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {user_imported_count} users'))
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {post_imported_count} posts'))

    def import_data(self, user_limit):
        user_imported_count = self.import_users(user_limit)
        post_imported_count = self.import_posts()
        return user_imported_count, post_imported_count

    def import_users(self, limit):
        url = 'https://jsonplaceholder.typicode.com/users'
        response = requests.get(url)
        users = response.json()[:limit]
        
        imported_count = 0
        existing_user_ids = set(User.objects.values_list('id', flat=True))
        for user in users:
            if user['id'] not in existing_user_ids:
                address_data = user.get('address', {})
                geo_data = address_data.pop('geo', {})
                company_data = user.get('company', {})

                geo, _ = Geo.objects.get_or_create(
                    lat=geo_data.get('lat'),
                    lng=geo_data.get('lng')
                )
                
                address, _ = Address.objects.get_or_create(
                    street=address_data.get('street'),
                    suite=address_data.get('suite'),
                    city=address_data.get('city'),
                    zipcode=address_data.get('zipcode'),
                    geo=geo
                )

                company, _ = Company.objects.get_or_create(
                    name_company=company_data.get('name'),
                    catchPhrase=company_data.get('catchPhrase'),
                    bs=company_data.get('bs')
                )

                User.objects.create(
                    id=user['id'],
                    name=user['name'],
                    username=user['username'],
                    email=user['email'],
                    phone=user.get('phone', ''),
                    website=user.get('website', ''),
                    address=address,
                    company=company
                )
                imported_count += 1

        return imported_count

    def import_posts(self):
        url = 'https://jsonplaceholder.typicode.com/posts'
        response = requests.get(url)
        posts = response.json()
        
        imported_count = 0
        existing_post_ids = set(Post.objects.values_list('id', flat=True))
        for post in posts:
            if post['id'] not in existing_post_ids:
                user_id = post.get('userId')
                if User.objects.filter(id=user_id).exists():
                    Post.objects.create(
                        id=post['id'],
                        userId_id=user_id,
                        title=post['title'],
                        body=post['body']
                    )
                    imported_count += 1

        return imported_count
