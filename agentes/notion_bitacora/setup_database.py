"""
setup_database.py

Crea la base de datos "Bitacora - Reto 30 Dias" dentro de una pagina de Notion,
con las propiedades correctas para el seguimiento diario del reto.

Se ejecuta UNA SOLA VEZ, al inicio del reto.

Requisitos previos:
1. Haber creado una integracion en https://www.notion.so/my-integrations
2. Haber compartido la pagina padre (donde vivira la base de datos) con esa integracion
3. Tener el token y el ID de la pagina padre en un archivo .env (ver .env.example)
"""

import os
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
PARENT_PAGE_ID = os.environ["NOTION_PARENT_PAGE_ID"]

notion = Client(auth=NOTION_TOKEN)


def crear_base_de_datos():
    nueva_bd = notion.databases.create(
        parent={"type": "page_id", "page_id": PARENT_PAGE_ID},
        title=[{"type": "text", "text": {"content": "Bitacora - Reto 30 Dias"}}],
        properties={
            # Propiedad titulo (obligatoria en toda base de datos de Notion)
            "Nombre": {"title": {}},
            "Dia": {"number": {"format": "number"}},
            "Semana": {
                "select": {
                    "options": [
                        {"name": "Semana 1", "color": "blue"},
                        {"name": "Semana 2", "color": "green"},
                        {"name": "Semana 3", "color": "yellow"},
                        {"name": "Semana 4", "color": "purple"},
                    ]
                }
            },
            "Estado": {
                "select": {
                    "options": [
                        {"name": "Pendiente", "color": "red"},
                        {"name": "En progreso", "color": "yellow"},
                        {"name": "Completado", "color": "green"},
                    ]
                }
            },
            "Horas invertidas": {"number": {"format": "number"}},
            "Link commit GitHub": {"url": {}},
            "Autoevaluacion (1-5)": {"number": {"format": "number"}},
        },
    )

    database_id = nueva_bd["id"]
    print("Base de datos creada exitosamente.")
    print(f"Database ID: {database_id}")
    print("\nGuarda este ID en tu .env como NOTION_DATABASE_ID para usarlo con add_bitacora_entry.py")
    return database_id


if __name__ == "__main__":
    crear_base_de_datos()
