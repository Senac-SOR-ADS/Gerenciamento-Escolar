import re
class EmailValidator:

    EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    @classmethod
    def is_valid_email(cls, email: str) -> bool:
        return re.match(cls.EMAIL_REGEX, email) is not None


if __name__ == "__main__":
    email = "caique.1+13@ferreira@gmail.com"

    if EmailValidator.is_valid_email(email):
        print("Email válido")
    else:
        print("Email inválido")
     