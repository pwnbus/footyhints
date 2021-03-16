from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


class LogoStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        """Forces removal of image file if already exists on disk

        Found at http://djangosnippets.org/snippets/976/
        """
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name
