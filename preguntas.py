"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    import csv

    with open("./data.csv", "r") as csvfile:
        reader_variable = csv.reader(csvfile, delimiter="	")
        rows = list(reader_variable)

    col1 = [row[1] for row in rows]

    return sum(map(int, col1))


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    import csv

    with open("./data.csv", "r") as csvfile:
        reader_variable = csv.reader(csvfile, delimiter="	")
        rows = list(reader_variable)

    col0 = [row[0] for row in rows]
    letters = sorted(set(col0))

    out = {}
    for letter in letters:
        out[letter] = col0.count(letter)

    return [(k, v) for k, v in out.items()]


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    import csv

    with open("./data.csv", "r") as csvfile:
        reader_variable = csv.reader(csvfile, delimiter="	")
        rows = list(reader_variable)

    col0 = [row[0] for row in rows]
    col1 = [row[1] for row in rows]

    letters = sorted(set(col0))

    out = {letter: 0 for letter in letters}
    for letter, num in zip(col0, col1):
        out[letter] += int(num)

    return [(k, v) for k, v in out.items()]


pregunta_03()


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    import csv

    with open("./data.csv", "r") as csvfile:
        reader_variable = csv.reader(csvfile, delimiter="	")
        rows = list(reader_variable)

    col3 = [row[2] for row in rows]
    months = [row.split("-")[1] for row in col3]
    unique_months = sorted(set(months))

    out = {}
    for month in unique_months:
        out[month] = months.count(month)

    return [(k, v) for k, v in out.items()]


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    import csv

    with open("./data.csv", "r") as csvfile:
        reader_variable = csv.reader(csvfile, delimiter="	")
        rows = list(reader_variable)

    col1 = [row[0] for row in rows]
    col2 = [row[1] for row in rows]

    letters = sorted(set(col1))

    out = {letter: [] for letter in letters}
    for letter, num in zip(col1, col2):
        out[letter].append(int(num))

    return [(k, max(v), min(v)) for k, v in out.items()]


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    import csv

    with open("./data.csv", "r") as csvfile:
        reader_variable = csv.reader(csvfile, delimiter="	")
        rows = list(reader_variable)

    col5 = [row[4] for row in rows]

    out = {}

    for row in col5:
        for register in row.split(","):
            key, value = register.split(":")
            if key not in out.keys():
                out[key] = []
            out[key].append(int(value))

    list_of_tuples = [(k, min(v), max(v)) for k, v in out.items()]

    return sorted(list_of_tuples, key=lambda x: x[0])


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    import csv

    with open("./data.csv", "r") as csvfile:
        reader_variable = csv.reader(csvfile, delimiter="	")
        rows = list(reader_variable)

    col0 = [row[0] for row in rows]
    col1 = [row[1] for row in rows]

    indexes = sorted(set(col1))
    out = {index: [] for index in indexes}
    for letter, num in zip(col0, col1):
        out[num].append(letter)

    return [(int(k), v) for k, v in out.items()]


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    import csv

    with open("./data.csv", "r") as csvfile:
        reader_variable = csv.reader(csvfile, delimiter="	")
        rows = list(reader_variable)

    col0 = [row[0] for row in rows]
    col1 = [row[1] for row in rows]

    indexes = sorted(set(col1))
    out = {index: [] for index in indexes}
    for letter, num in zip(col0, col1):
        out[num].append(letter)

    return [(int(k), sorted(set(v))) for k, v in out.items()]


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    import csv

    with open("./data.csv", "r") as csvfile:
        reader_variable = csv.reader(csvfile, delimiter="	")
        rows = list(reader_variable)

    col5 = [row[4] for row in rows]

    out = {}

    for row in col5:
        for register in row.split(","):
            key, value = register.split(":")
            if key not in out.keys():
                out[key] = 0
            out[key] += 1

    return dict(sorted(out.items()))


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    import csv

    with open("./data.csv", "r") as csvfile:
        reader_variable = csv.reader(csvfile, delimiter="	")
        rows = list(reader_variable)

    col1 = [row[0] for row in rows]
    col4 = [row[3] for row in rows]
    col5 = [row[4] for row in rows]

    out = []
    for row_col1, row_col4, row_col5 in zip(col1, col4, col5):
        out.append((
            row_col1, len(row_col4.split(",")), len(row_col5.split(","))
        ))

    return out


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """

    import csv

    with open("./data.csv", "r") as csvfile:
        reader_variable = csv.reader(csvfile, delimiter="	")
        rows = list(reader_variable)

    col2 = [row[1] for row in rows]
    col4 = [row[3] for row in rows]

    out = {}
    for row_col2, row_col4 in zip(col2, col4):
        for letter in row_col4.split(","):
            if letter not in out.keys():
                out[letter] = 0
            out[letter] += int(row_col2)

    return dict(sorted(out.items()))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

    import csv

    with open("./data.csv", "r") as csvfile:
        reader_variable = csv.reader(csvfile, delimiter="	")
        rows = list(reader_variable)

    col1 = [row[0] for row in rows]
    col5 = [row[4] for row in rows]

    out = {}
    for letter, row_col5 in zip(col1, col5):

        if letter not in out.keys():
            out[letter] = 0

        out[letter] += sum([int(val.split(":")[1]) for val in row_col5.split(",")])

    return dict(sorted(out.items()))
