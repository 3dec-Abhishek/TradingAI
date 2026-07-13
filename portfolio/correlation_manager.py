import numpy as np

class CorrelationManager:

    def correlation(self, returns):

        return np.corrcoef(returns,rowvar=False)