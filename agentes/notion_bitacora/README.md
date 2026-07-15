# Automatizacion de Bitacora en Notion

Este modulo conecta tu bitacora de Notion con la consola, para que puedas
crear la base de datos y registrar tu progreso diario sin abrir el navegador.

## Paso 0 - Preparacion (una sola vez)

1. Crea una integracion en https://www.notion.so/my-integrations
   - Nombrala "Bitacora Reto 30 Dias"
   - Copia el token secreto que te da (empieza con "secret_" o "ntn_")

2. Crea o elige una pagina en Notion donde vivira tu base de datos
   (por ejemplo, una pagina llamada "Reto 30 Dias - IA").

3. Comparte esa pagina con tu integracion:
   Abre la pagina -> boton "..." arriba a la derecha -> "Connections" ->
   busca y selecciona tu integracion.

4. Copia el ID de esa pagina desde su URL. Tiene esta forma:
   https://www.notion.so/tu-workspace/Reto-30-Dias-IA-1a2b3c4d5e6f7890abcdef1234567890
   El ID son los 32 caracteres al final (sin guiones necesariamente).

## Paso 1 - Instalar dependencias

```bash
cd agentes/notion_bitacora
pip install -r requirements.txt
```

## Paso 2 - Configurar credenciales

```bash
cp .env.example .env
```

Edita `.env` y coloca tu `NOTION_TOKEN` y `NOTION_PARENT_PAGE_ID`.

## Paso 3 - Crear la base de datos (una sola vez)

```bash
python setup_database.py
```

Esto imprime un `NOTION_DATABASE_ID`. Copialo y agregalo a tu archivo `.env`.

## Paso 4 - Registrar tu progreso cada noche

```bash
python add_bitacora_entry.py \
  --dia 1 \
  --semana "Semana 1" \
  --tema "Que es un LLM - tokens y context window" \
  --estado "Completado" \
  --horas 2 \
  --commit "https://github.com/Leonardodocs21/30-dias-llm-agentes-if/commit/TU_HASH" \
  --autoeval 4
```

Esto crea automaticamente una nueva entrada en tu base de datos de Notion,
con el formato correcto y lista para revisar.

## Idea de mejora futura (semana 4 - multiagente)

Este script es intencionalmente simple: un solo "agente" que hace una tarea.
Cuando lleguemos a la semana de sistemas multi-agente, este mismo modulo se
puede dividir en:
- Un agente que lee tu ultimo commit de GitHub automaticamente (via API de GitHub)
- Un agente que redacta el resumen del dia a partir del diff del commit
- Un agente que registra la entrada en Notion (este script, sin cambios)

Es un buen ejemplo de como un mismo proyecto crece de "script simple" a
"sistema multi-agente" sin reescribir todo desde cero.
