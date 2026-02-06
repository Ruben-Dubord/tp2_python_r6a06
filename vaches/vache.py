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

    def __init__(self, petitNom, poids):
        if petitNom is None or petitNom.strip() == "":
            raise InvalidVacheException

        if poids is None or poids < self.POIDS_PANSE_VIDE:
            raise InvalidVacheException

        self._petitNom = petitNom
        self._poids = poids
        self._panse = self.POIDS_PANSE_VIDE
        self._age = self.AGE_NAISSANCE
        self._id = self.NEXT_ID
        Vache.NEXT_ID += 1


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

    def valider_rumination_possible(self):
        if self._panse <= self.POIDS_PANSE_VIDE:
            raise InvalidVacheException
        return True

    def _calculer_lait(self, panse_avant):
        return 0.0

    def _stocker_lait(self, lait = None):
        return

    def _post_rumination(self, panse_avant, lait = None):
        return

    def ruminer(self):

        self.valider_rumination_possible()

        panse_avant = self._panse
        gain = self.RENDEMENT_RUMINATION * panse_avant
        self._poids += gain

        self._calculer_lait(panse_avant)
        self._stocker_lait()

        self._panse = self.POIDS_PANSE_VIDE

        self._post_rumination(panse_avant)