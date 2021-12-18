from dataclasses import dataclass

@dataclass
class Cell:
    risk: int
    best_risk = float("inf")

    def offer_better_risk(self, risk_offer: int):
        if risk_offer < self.best_risk:
            self.best_risk = risk_offer
