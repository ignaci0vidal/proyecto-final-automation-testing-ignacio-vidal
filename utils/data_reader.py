import csv
import pathlib


def leer_usuarios_csv():
    archivo = pathlib.Path("data/users.csv")

    with archivo.open(
        mode="r",
        encoding="utf-8",
        newline=""
    ) as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)


def obtener_casos_login(): 
    usuarios = leer_usuarios_csv()

    return [
        (
            usuario["username"],
            usuario["password"],
            usuario["expected_result"]
        )
        for usuario in usuarios
    ]