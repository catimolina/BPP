class operaciones_finanzas:
    """
    Operaciones finanzas:
    Es una clase que permite calcular la respuesta a las preguntas de la primera práctica de la asignatura
    dado un archivo csv que contenga la información de los ingresos y gastos a lo largo de un año.

    Atributos:
        op1: Dataframe que contiene los datos de los ingresos y gastos a lo largo de un año.

    Métodos:
        max_gastos:
            Devuelve el mes en que más se ha gastado de op1
        gasto_total:
            Devuelve el gato total a lo largo del año de op1
        media_gastos:
            Devuelve el la media de gasto por mes a lo largo del año de op1
        max_ahorro:
            Devuelve el mes en que más se ha ahorrado de op1
        ingresos_totales:
            Devuelve el ingreso total a lo largo del año de op1

    >>> import operaciones_finanzas
    >>> of = operaciones_finanzas(df)
    """

    def __init__(self,op1):
        self.op1 = op1

    def max_gastado(self):
        """
        Método max_gasto que nos permite resolver la pregunta: ¿Qué mes se ha gastado más?
        Input:
            La entrada es un Dataframe con los datos de los ingrsos y gastos a lo largo de un año.
        Output:
            Número del mes en que más se ha gastado segun los datos proporcionados.
        """
        aux = []
        df = self.op1
        for row in df:
            aux.append(0)
            for i in df[row]:
                try:
                    i = int(i)
                    if i < 0:
                        aux[-1] += i
                except ValueError:
                    aux[-1] += 0
        return aux.index(min(aux)) + 1

    def gasto_total(self):
        """
        Método gasto_total que nos permite resolver la pregunta: ¿Cuál ha sido el gasto total a lo largo del año?
        Input:
            La entrada es un Dataframe con los datos de los ingrsos y gastos a lo largo de un año.
        Output:
            Gasto total a lo largo del año.
        """
        aux = []
        df = self.op1
        for row in df:
            aux.append(0)
            for i in df[row]:
                try:
                    i = int(i)
                    if i < 0:
                        aux[-1] += i
                except ValueError:
                    aux[-1] += 0
        return -sum(aux)

    def media_gastos(self):
        """
        Método media_gastos que nos permite resolver la pregunta: ¿Cuál es la media de gastos al año?
        Input:
            La entrada es un Dataframe con los datos de los ingrsos y gastos a lo largo de un año.
        Output:
            Media de gastos por mes durante el año.
        """
        aux = []
        df = self.op1
        for row in df:
            aux.append(0)
            for i in df[row]:
                try:
                    i = int(i)
                    if i < 0:
                        aux[-1] += i
                except ValueError:
                    aux[-1] += 0
        return -round(sum(aux)/12,2)

    def max_ahorro(self):
        """
        Método max_ahorro que nos permite resolver la pregunta: ¿Qué mes se ha ahorrado más?
        Input:
            La entrada es un Dataframe con los datos de los ingrsos y gastos a lo largo de un año.
        Output:
            Numéro del mes en que más se ha ahorrado a lo largo del año.
        """
        aux = []
        df = self.op1
        for row in df:
            aux.append(0)
            for i in df[row]:
                try:
                    i = int(i)
                    aux[-1] += i
                except ValueError:
                    aux[-1] += 0
        return aux.index(max(aux)) + 1

    def ingresos_totales(self):
        """
        Método ingresos_totales que nos permite resolver la pregunta: ¿Cuáles han sido los ingresos totales a lo largo del año?
        Input:
            La entrada es un Dataframe con los datos de los ingrsos y gastos a lo largo de un año.
        Output:
            Ingreso total a lo largo del año.
        """
        aux = []
        df = self.op1
        for row in df:
            aux.append(0)
            for i in df[row]:
                try:
                    i = int(i)
                    if i > 0:
                        aux[-1] += i
                except ValueError:
                    aux[-1] += 0
        return sum(aux)
