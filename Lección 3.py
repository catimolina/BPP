import pandas as pd
import numpy as np
from utils import operaciones

if __name__ == "__main__":
    finanzas = pd.read_csv('finanzas2020.csv', sep = '\t')
    of = operaciones.operaciones_finanzas(finanzas)
    print(of.media_gastos())
