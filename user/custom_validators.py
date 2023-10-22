from django.core.exceptions import ValidationError

class NonEmptyPasswordValidator:
    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ("The password must be at least %(min_length)d character(s) long."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return (
            "The password must be at least %(min_length)d character(s) long."
        ) % {'min_length': self.min_length}