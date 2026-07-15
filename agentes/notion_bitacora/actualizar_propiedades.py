"""
actualizar_propiedades.py

Migra la base de datos de Notion ya existente, agregando las propiedades
necesarias para el sistema de reacondicionamiento (repaso), SIN borrar
ninguna entrada ni propiedad existente.

Se ejecuta UNA SOLA VEZ, despues de adoptar el sistema de checkpoints.

Requiere que NOTION_DATABASE_ID ya este definido en tu .env
(es decir, que ya hayas corrido setup_database.py antes).
"""

import os
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

notion = Client(auth=NOTION_TOKEN)


def agregar_propiedades_de_repaso():
    notion.databases.update(
        database_id=DATABASE_ID,
        properties={
            "Tema nuevo": {"rich_text": {}},
            "Temas repasados": {"rich_text": {}},
        },
    )
    print("Propiedades 'Tema nuevo' y 'Temas repasados' agregadas correctamente.")
    print("Tus entradas anteriores no se modificaron ni se perdieron.")


if __name__ == "__main__":
    agregar_propiedades_de_repaso()
