class Human:
    def __init__(self, name, last_name, date_of_birth,):
        self.__name = name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth

    @property
    def name(self):
        return self.__name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def data_of_birth(self):
        return self.__date_of_birth


class Doctor(Human):
    def __init__(self, name, last_name, date_of_birth, medical_degree):
        super().__init__(name, last_name, date_of_birth)
        self.__medical_degree = medical_degree

    @property
    def medical_degree(self):
        return self.__medical_degree


class Soldier(Human):
    pass


class Pilot(Human):
    pass


doctor = Doctor(
    name='Aibek',
    last_name='Akmaraliev',
    date_of_birth='01.01.01',
    medical_degree='high'
)

soldier = Soldier(
    name='Bekjan',
    last_name = 'Akunov',
    date_of_birth='06.12.1996'

)






