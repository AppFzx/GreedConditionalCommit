# greed.py - prototype implementation demoing test && commit || revert

class Greed:
    """ Hold dice and evaluate scores for rolls """
    def __init__(self, dice = []):
        self.dice = dice

    def __str__(self):
        return ','.join(self.dice)

    def __repr__(self):
        return ','.join(self.dice)

    @classmethod
    def rollRandom(cls, )

    def getScore(self):
        return 0

if __name__ == "__main__":
    g = Greed()