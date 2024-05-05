from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser



# from django.contrib.auth.models import User



class User(AbstractUser):
    pass

def user_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class User_File_Upload(models.Model):
    user=models.ForeignKey(get_user_model(),models.SET_NULL, blank=True, null=True)
    photo = models.ImageField(blank=True, upload_to=user_directory_path,default=None, null=True )
    is_avatar=models.BooleanField(default=False)

    @staticmethod
    def set_default_image(user):
        user_file_upload=User_File_Upload(user=user, photo='/default.jpg', is_avatar=True)
        user_file_upload.save()