from stdnum import iban


class Documentation:

    @staticmethod
    def verify_docs(doc_number):
        if len(doc_number) == 9 or len(doc_number) == 8:
            return Ppsn(doc_number)
        if 15 <= len(doc_number) <= 32:
            return IbanNumber(doc_number)
        else:
            raise ValueError("The quantity of digits is incorrect!!")


class Ppsn:

    def __init__(self, doc_number):
        doc_number = doc_number.strip().upper()
        if self.validation(doc_number):
            self.ppsn = doc_number
        else:
            raise ValueError("PPSN Invalid!!")

    def validation(self, doc_number):
        numbers = doc_number[:7]
        letters = doc_number[7:]
        if letters.isalpha() and numbers.isalnum():
            return True
        else:
            return False

    def __str__(self):
        return self.ppsn


class IbanNumber:

    def __init__(self, doc_number):
        if self.validation(doc_number):
            self.iban = doc_number
        else:
            raise ValueError("Iban Invalid!!")

    def validation(self, doc_number):
        doc_number = doc_number.strip().upper()
        return iban.is_valid(doc_number, check_country=True)

    def format_number(self):
        return iban.format(self.iban, separator=' ')

    def __str__(self):
        return self.format_number()