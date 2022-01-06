from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('У пользователей должен быть адрес электронной почты.')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_admin=is_admin,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password=None):
        return self.create_user(email, password, True, False)

    def create_superuser(self, email, password=None):
        return self.create_user(email, password, True, True)


class User(AbstractBaseUser):
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=150, blank=True, null=True)
    last_name = models.CharField('last name', max_length=150, blank=True, null=True)
    phone_number = models.CharField('phone number', max_length=15, blank=True, null=True)
    birthday = models.DateField('birthday', blank=True, null=True)
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text=(
            'Определяет, следует ли считать этого пользователя активным.'
            'Снимите этот флажок вместо удаления учетных записей.')
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Определяет, может ли пользователь войти как администратор.'
    )
    is_admin = models.BooleanField(
        'superuser status',
        default=False,
        help_text='Определяет, может ли пользователь войти как суперюзер.'
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True