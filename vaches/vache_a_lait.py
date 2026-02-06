from typing import Any

from vaches.exceptions import InvalidVacheException
from vaches.vache import Vache

class VacheALait(Vache):

    RENDEMENT_LAIT = 1.1
    PRODUCTION_LAIT_MAX = 40.0
    PAS_DE_LAIT = 0.0


    def __init__(self, petitNom, poids):

        super().__init__(petitNom, poids)

        self._lait_disponible = self.PAS_DE_LAIT
        self._lait_total_produit = self.PAS_DE_LAIT
        self._lait_total_traite = self.PAS_DE_LAIT


    def __str__(self):
        return ""

    @property
    def lait_disponible(self):
        return self._lait_disponible

    @property
    def lait_total_produit(self):
        return self._lait_total_produit

    @property
    def lait_total_traite(self):
        return self._lait_total_traite

    def _calculer_lait(self, panse_avant):
        lait = self.RENDEMENT_LAIT * panse_avant
        return lait

    def _stocker_lait(self, lait):
        self._lait_total_produit += lait
        self._lait_disponible += lait

    def traire(self, litres):
        if not (0 < litres <= self._lait_disponible):
            raise InvalidVacheException
        else:
            self._lait_disponible -= litres
            self._lait_total_traite += litres

            return litres

    def valider_rumination_possible(self):
        super().valider_rumination_possible()

        lait_futur = self.RENDEMENT_LAIT * self._panse
        if self._lait_disponible + lait_futur > self.PRODUCTION_LAIT_MAX:
            raise InvalidVacheException
