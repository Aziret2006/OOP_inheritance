# Super class parameter 3 attr and 2 methods
# Child class +2 attr +2 methods (3 child class)


class Insects:
    def __init__(self, type, body, antennae, venom=None):
        self.__type = type
        self.__body = body
        self.__anntennae = antennae
        self.__venom = venom

    @property
    def type(self):
        return self.__type

    @property
    def body(self):
        return self.__body

    @property
    def anntennae(self):
        return self.__anntennae

    @property
    def venom(self):
        return self.__venom


    def type(self):
        print(f"{self.__type} my type")


    def crawl(self):
        print("crawl")


class Butterfly(Insects):
    def __init__(self, type, body, antennae, venom, wings, caterpillar_first):
        super().__init__(type, body, antennae, venom)
        self.__wings = wings
        self.__caterpillar_first = caterpillar_first

    @property
    def wings(self):
        return self.__wings

    @property
    def caterpillar_first(self):
        return self.__caterpillar_first

    def fly(self):
        print("Flying")


class Grasshopper(Insects):
    def __init__(self, type, body, antennae, venom, long_legs, singer):
        super().__init__(type, body, antennae, venom)
        self.__long_legs = long_legs
        self.__singer = singer

    @property
    def long_legs(self):
        return self.__long_legs

    @property
    def singer(self):
        return self.__singer

    def jump(self):
        print("High jumping")

    def sing(self):
        print("S-s-s")


class Ant(Insects):
    def __init__(self, type, body, antennae, venom, jaw, strong):
        super().__init__(type, body, antennae, venom)
        self.__jaw = jaw
        self.__strong = strong

    @property
    def jaw(self):
        return self.__jaw

    @property
    def strong(self):
        return self.__strong

    def bite(self):
        print("Strong bite")

    def lifting(self):
        print("Lifts 100 times its own weight")




