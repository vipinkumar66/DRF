"""
Making the custom permissions for our users => SPECIALLY RELATED TO DJANGO MODEL PERMISSIONS
"""

from rest_framework import permissions

class IsStaffEditorPermissions(permissions.DjangoModelPermissions):
    """
    Here we are going to handle the permissions based on the
    models, that we do in the django admin
    """
    # def has_permission(self, request, view):
    #     """
    #     The disadvantage of giving the permissions like this is that
    #     if any of the permission is there it will return True and than
    #     it will be true for others too
    #     """
    #     user = request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm("products.add_product"):
    #             return True
    #         if user.has_perm("products.change_product"):
    #             return True
    #         if user.has_perm("products.delete_product"):
    #             return True
    #         if user.has_perm("products.view_product"): #appName.action_model
    #                 return True
    #         return False
    #     return False
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)

