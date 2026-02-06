from vaches.exceptions import InvalidVacheException
class Vache:

    AGE_NAISSANCE = 0
    AGE_MAX = 25
    POIDS_MAX = 1000.0
    PANSE_MAX = 50.0
    POIDS_PANSE_VIDE = 0.0
    RENDEMENT_RUMINATION = 0.25
    COEFFICIENT_NUTRITIONNEL = None
    NEXT_ID = 1

    def __init__(self, petitNom, poids, age=AGE_NAISSANCE):
        if petitNom is None or petitNom.strip() == '':
            raise InvalidVacheException

        if poids is None or poids < self.POIDS_PANSE_VIDE:
            raise InvalidVacheException

        self._age = age
        if not (self.AGE_NAISSANCE <= self._age <= self.AGE_MAX):
            raise InvalidVacheException

        else:
            self._petitNom = petitNom
            self._poids = poids
            self._panse = self.POIDS_PANSE_VIDE
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
        if self._age >= self.AGE_MAX:
            raise InvalidVacheException
        self._age += 1

    def brouter(self, quantite, nourriture=None):
        if quantite <= 0:
            raise InvalidVacheException

        if nourriture is not None:
            raise InvalidVacheException

        if self._panse + quantite > self.PANSE_MAX:
            raise InvalidVacheException

        self._panse += quantite