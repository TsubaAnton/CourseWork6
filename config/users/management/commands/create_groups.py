from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    def handle(self, *args, **options):
        groups = [
            {'name': 'managers', 'description': 'Менеджеры'}
        ]

        permissions = [
            'add_client',
            'change_client',
            'delete_client',
            'view_client',
            'add_newsletter',
            'change_newsletter',
            'delete_newsletter',
            'view_newsletter',
        ]

        for group_data in groups:
            group, created = Group.objects.get_or_create(name=group_data['name'])
            if created:
                group.description = group_data['description']
                group.save()

            for perm in permissions:
                try:
                    # Get permission object
                    permission = Permission.objects.get(codename=perm)
                    # Add permission to group
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Permission {perm} not found.'))

            group.save()
            self.stdout.write(self.style.SUCCESS(f'Group {group.name} with permissions created or updated.'))
