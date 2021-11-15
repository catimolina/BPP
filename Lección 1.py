# Importación de las librerías
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Error(Exception):
    pass
class ErrorMeses(Error):
    pass
class ErrorIndice(Error):
    pass


# Comprobamos que el fichero existe
try:
    df = pd.read_csv('finanzas2020.csv', sep = '\t')
    print(df)

    # Comprobamos que el fichero tiene 12 columnas, una para cada mes del año.
    try:
        if len(df.columns) == 12:

            # Comprobamos que cada mes tenga contenido
            for row in df:
                try:
                    len(df[df[row]!=''].index) < 2
                except ErrorIndice:
                    print("Hay un mes sin contenido")

            # ¿Qué mes se ha gastado más?
            aux = []
            for row in df:
                aux.append(0)
                for i in df[row]:
                    # Comprobamos que todos los datos son correctos
                    try:
                        i = int(i)
                        if i < 0:
                            aux[-1] += i
                    except ValueError:
                        aux[-1] += 0
                print(f"En {row} se ha gastado {-aux[-1]}")
            print(f"\nEl mes que más se ha gastado ha sido el {aux.index(min(aux)) + 1}^o \n\n")

            #¿Cuál ha sido el gasto total a lo largo del año?
            print(f"El gasto total a lo largo del año: {-sum(aux)}\n\n")

            # ¿Cuál es la media de gastos al año?
            print(f"Media de gastos al año: {-round(sum(aux)/12,2)} por mes\n\n")

            # ¿Qué mes se ha ahorrado más?
            aux = []
            for row in df:
                aux.append(0)
                for i in df[row]:
                    # Comprobamos que todos los datos son correctos
                    try:
                        i = int(i)
                        aux[-1] += i
                    except ValueError:
                        aux[-1] += 0
                print(f"En {row} se ha ahorrado {aux[-1]}")
            print(f"\nEl mes que más se ha ahorrado ha sido el {aux.index(max(aux)) + 1}^o \n\n")

            # ¿Cuáles han sido los ingresos totales a lo largo del año?
            aux = []
            for row in df:
                aux.append(0)
                for i in df[row]:
                    # Comprobamos que todos los datos son correctos
                    try:
                        i = int(i)
                        if i > 0:
                            aux[-1] += i
                    except ValueError:
                        aux[-1] += 0
            print(f"Ingresos totales a lo largo del año: {sum(aux)} \n\n")

            # OPCIONAL: Realice una gráfica de la evolución de ingresos a lo largo del año.
            # Gráfica 1
            plt.plot(aux)
            plt.title("Evolución de los ingresos")
            plt.xlabel("Meses")
            plt.ylabel("Euros")
            plt.show()
            # Gráfica 2
            meses = list(df.columns.values)
            posicion_y = np.arange(len(meses))
            plt.barh(posicion_y, aux, align = "center")
            plt.yticks(posicion_y, meses)
            plt.title("Evolución de los ingresos")
            plt.ylabel("Meses")
            plt.xlabel("Euros")
            plt.show()

        else:
            raise ErrorMeses

    except ErrorMeses:
        print("El archivo no tiene 12 columnas")

except IOError as error:
    print("No se encuentra el fichero o no puede ser leído. Error: ", error)
    
