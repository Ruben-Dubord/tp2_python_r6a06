from vaches.vache import Vache

class NoMilkStrategy():

    def calculer_lait(self, vache:"Vache", panse_avant: float):
        return 0.0

    def stocker_lait(self):
        return

    def post_rumination(self, vache:"Vache", lait: float, panse_avant: float):
        return


strategy: RuminationStrategy = NoMilkStrategy