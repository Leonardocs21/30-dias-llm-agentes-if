"""
add_bitacora_entry.py

Anade una entrada diaria a tu bitacora de Notion, calculando automaticamente
que temas corresponde repasar segun el sistema de reacondicionamiento
(ver agentes/reinforcement/calcular_repaso.py).

Uso (solo necesitas indicar el dia y los datos de la sesion; el tema nuevo
y el repaso se calculan solos):

    python add_bitacora_entry.py \
        --dia 5 \
        --semana "Semana 1" \
        --estado "Completado" \
        --horas 2 \
        --commit "https://github.com/Leonardocs21/30-dias-llm-agentes-if/commit/abc123" \
        --autoeval 4
"""

import os
import sys
import argparse
from pathlib import Path
from notion_client import Client
from dotenv import load_dotenv

# Permite importar el modulo de reacondicionamiento desde su carpeta hermana
sys.path.append(str(Path(__file__).resolve().parent.parent / "reinforcement"))
from calcular_repaso import resumen_del_dia, formatear_repaso_texto

load_dotenv()

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

notion = Client(auth=NOTION_TOKEN)


def agregar_entrada(dia, semana, estado, horas, commit_url, autoeval):
    resumen = resumen_del_dia(dia)
    tema_nuevo = resumen["tema_nuevo"]
    temas_repaso_texto = formatear_repaso_texto(resumen["temas_repaso"])

    nombre_pagina = f"Dia {dia} - {tema_nuevo}"

    nueva_pagina = notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "Nombre": {"title": [{"text": {"content": nombre_pagina}}]},
            "Dia": {"number": dia},
            "Semana": {"select": {"name": semana}},
            "Estado": {"select": {"name": estado}},
            "Horas invertidas": {"number": horas},
            "Link commit GitHub": {"url": commit_url},
            "Autoevaluacion (1-5)": {"number": autoeval},
            "Tema nuevo": {"rich_text": [{"text": {"content": tema_nuevo}}]},
            "Temas repasados": {"rich_text": [{"text": {"content": temas_repaso_texto}}]},
        },
    )

    print(f"Entrada creada: {nombre_pagina}")
    print(f"Repaso de hoy: {temas_repaso_texto}")
    print(f"URL en Notion: {nueva_pagina['url']}")


def parse_args():
    parser = argparse.ArgumentParser(description="Agrega una entrada diaria a la bitacora de Notion")
    parser.add_argument("--dia", type=int, required=True, help="Numero del dia (1-30)")
    parser.add_argument("--semana", type=str, required=True, choices=["Semana 1", "Semana 2", "Semana 3", "Semana 4"])
    parser.add_argument("--estado", type=str, default="Completado", choices=["Pendiente", "En progreso", "Completado"])
    parser.add_argument("--horas", type=float, required=True, help="Horas invertidas ese dia")
    parser.add_argument("--commit", type=str, required=True, help="URL del commit de GitHub del dia")
    parser.add_argument("--autoeval", type=int, required=True, choices=[1, 2, 3, 4, 5], help="Autoevaluacion del 1 al 5")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    agregar_entrada(args.dia, args.semana, args.estado, args.horas, args.commit, args.autoeval)
