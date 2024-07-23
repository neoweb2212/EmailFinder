import re

class EmailValidationPipeline:
    def process_item(self, item, spider):
        if 'email' in item:
            if self.is_valid_email(item['email']):
                return item
            else:
                return None  # Drop the item if the email is not valid
        return item

    def is_valid_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None
