from eve.io.mongo import Validator
from email_validator import validate_email, EmailNotValidError

class MyValidator(Validator):
    def _validate_isemail(self, isemail, field, value):
        if isemail:
            try:
                email_info = validate_email(value)
                value = email_info.normalized
                
            except EmailNotValidError as _:
                self._error(field, "Invalid email address")

