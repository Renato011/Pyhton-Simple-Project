import re


class PhoneNumber:
    def __init__(self, phone_number):
        if self.phone_verification(phone_number):
            self.number = phone_number
        else:
            raise ValueError("Incorrect number!")


    def __str__(self):
        return self.format_number()


    def phone_verification(self, phone_number):
        parttern = "([0-9]{2,3})?([0-9]{2,3})([0-9]{3,4})([0-9]{4})"
        answer = re.findall(parttern, phone_number)
        if answer:
            return True
        else:
            return False

    def format_number(self):
        parttern = "([0-9]{2,3})?([0-9]{2,3})([0-9]{3,4})([0-9]{4})"
        answer = re.search(parttern, self.number)
        formatted_number = "+{}({}){}-{}".format(
            answer.group(1),
            answer.group(2),
            answer.group(3),
            answer.group(4)

        )
        return formatted_number