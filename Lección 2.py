import pandas as pd
import leccion1
import pytest


df = pd.read_csv('finanzas2020.csv', sep = '\t')


def test_max_gastado():
    assert leccion1.max_gastado(df) == 4

def test_gasto_total():
    assert leccion1.gasto_total(df) == 296791

def test_media_gatos():
    assert leccion1.media_gatos(df) == 24732.58

def test_max_ahorro():
    assert leccion1.max_ahorro(df) == 1

def test_ingresos_totales():
    assert leccion1.ingresos_totales(df) == 280961
