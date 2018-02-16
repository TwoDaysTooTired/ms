from sim.models import StudentUser


class MyCustomBackend:

    def authenticate(self, serialNum=None, password=None):
        try:
            user = StudentUser.objects.get(SerialNum=serialNum)
        except StudentUser.DoesNotExist:
            pass
        else:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return StudentUser.objects.get(pk=user_id)
        except StudentUser.DoesNotExist:
            return None
