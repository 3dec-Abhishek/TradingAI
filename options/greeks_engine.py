import math


class GreeksEngine:



    def delta(
        self,
        option_type,
        probability
    ):


        if option_type=="CALL":

            return probability


        return probability-1




    def gamma(
        self,
        volatility
    ):


        return (
            1 /
            (
                volatility+0.01
            )
        )




    def theta(
        self,
        days
    ):


        return -1/days




    def vega(
        self,
        volatility
    ):


        return volatility*0.1