from unicodedata import category


class product():
    def set_category(self, category):
        self._category = category

    def get_category(self, category):
        self._category = category

    category = property(fget=get_category, fset= set_category)

p = product()
p.category = 'something'

print(p)
print(p.__dict__)
