import vaches.exceptions.InvalidVacheException
class Vache:

    AGE_MAX = 25
    POIDS_MAX = 1000.0
    PANSE_MAX = 50.0
    POIDS_MIN_PANSE = 2.0
    RENDEMENT_RUMINATION = 0.25
    COEFFICIENT_NUTRITIONNEL = None
    NEXT_ID = 1

    def __init__(self, petitNom, poids, age):
        self._petitNom = petitNom
        self._age = age
        self._poids = poids
        self._panse = self.POIDS_MIN_PANSE
        self._id = self.NEXT_ID
        self.NEXT_ID += 1

    @property
    def petitNom(self) -> None:
        return self._petitNom

    @property
    def age(self) -> None:
        return self._age

    @property
    def poids(self) -> None:
        return self._poids

    @property
    def panse(self) -> None:
        return self._panse

    def __str__(self):
        return ""

    def vieillir(self):
        self._age += 1

    def brouter(self, quantite = 1.0, nourriture = None):
        if quantite <= 0:
            raise vaches.exceptions.InvalidVacheException
        else:
            self._panse += quantite
            if self._panse > self.PANSE_MAX:
                raise vaches.exceptions.InvalidVacheException