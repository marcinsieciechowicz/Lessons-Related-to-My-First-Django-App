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

My_family = Nicolas('Sieciechowicz', 'Mikolaj')
My_family.surname()
My_family.name()
My_fam = Fam_member('Sieciechowicz')
My_fam.surname()
print(My_fam.l_name)


