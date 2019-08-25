from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from account.models import Account



content_type = ContentType.objects.get_for_model(Account)
permission = Permission.objects.create(
    codename='can_delete',
    name='Can Delete Users',
    content_type=content_type,
)






new_group, created = Group.objects.get_or_create(name='new_group')
# Code to add permission to group ???
ct = ContentType.objects.get_for_model(Project)

# Now what - Say I want to add 'Can add project' permission to new_group?
permission = Permission.objects.create(codename='can_add_project',
                                   name='Can add project',
                                   content_type=ct)
new_group.permissions.add(permission)


special_users = Group(name='Special Users')