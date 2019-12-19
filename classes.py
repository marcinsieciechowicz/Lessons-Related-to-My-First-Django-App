class Fam_member:
    def __init__(self, surname):
        self.l_name = surname

    def surname(self):
        print(self.l_name)


class Nicolas(Fam_member):
    def __init__(self, surname, f_name):
        super().__init__(surname)
        self.f_name = f_name

    def name(self):
        print(self.f_name)

    def full_name(self):
        print(self.f_name, self.l_name)

nico = Nicolas('Sieciechowicz', 'Mikolaj')
nico.surname()
nico.name()
nico.full_name()
fam_mem = Fam_member('Sieciechowicz')
fam_mem.surname()

