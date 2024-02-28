from .permissions import IsStaffEditorPermissions
from rest_framework import permissions

class StaffEditorPermissionMixins():
    permission_class = [permissions.IsAdminUser, IsStaffEditorPermissions]