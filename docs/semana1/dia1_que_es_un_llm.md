# Semana 1 · Día 1 — ¿Qué es realmente un LLM?

**Duración estimada:** 2 horas
**Objetivo del día:** entender qué son los tokens y cómo un modelo "lee" y "genera" texto.

---

## 1. Teoría (40 min)

Un LLM (Large Language Model) no lee palabras — lee **tokens**. Un token puede ser una palabra completa, parte de una palabra, o incluso un signo de puntuación. Por ejemplo, "inteligencia artificial" puede dividirse en 3-4 tokens dependiendo del modelo.

**¿Por qué te importa esto como analista financiero?**
- Cada consulta que le haces a Claude/GPT sobre un documento largo (ej. una normativa RECA) consume tokens tanto en la pregunta como en la respuesta.
- El modelo tiene un **context window** (ventana de contexto): un límite de tokens que puede "ver" a la vez. Si tu documento supera ese límite, el modelo simplemente no lo ve completo — de ahí surgen respuestas incompletas o alucinadas.
- La **temperature** controla cuán "creativo" o "determinista" es el modelo. Para análisis financiero, quieres temperature baja (respuestas consistentes); para brainstorming, puede ser más alta.

**Recursos para hoy (elige uno, no los tres):**
- Video "But what is a GPT?" de 3Blue1Brown (visualización excelente, ~25 min) — búscalo en YouTube
- Documentación de Anthropic sobre cómo funcionan los modelos: https://docs.claude.com/en/docs/about-claude/models/overview
- Si prefieres texto corto: busca "tokenización LLM explicación" y lee 2 artículos cortos

## 2. Práctica (50 min)

**Ejercicio 1 — Contar tokens a mano**
Ve a https://platform.openai.com/tokenizer o usa la librería `tiktoken` en Python y prueba con 3 frases:
1. Una frase corta en español
2. Un párrafo técnico de un documento RECA/RL9 real (sin datos sensibles, solo estructura)
3. La misma frase en inglés

Anota: ¿el español usa más o menos tokens que el inglés para decir lo mismo? (Spoiler: normalmente más — es relevante para tu trabajo si alguna vez optimizas costos de API).

**Ejercicio 2 — Ver el límite de contexto en acción**
Abre una conversación nueva con Claude o Opencode y pégale un documento largo (puede ser público, ej. un artículo largo de Wikipedia). Pregúntale algo sobre la última línea del documento. Luego pégale un documento 5 veces más largo y repite. Observa si la calidad de la respuesta cambia.

## 3. Evaluación del día (30 min)

En tu bitácora de Notion, escribe **sin mirar tus notas** una respuesta corta (2-3 líneas cada una) a:

1. ¿Qué es un token y por qué no es lo mismo que una palabra?
2. ¿Qué es el context window y qué pasa si lo excedes?
3. ¿Qué controla la temperature y qué valor usarías para análisis financiero vs. brainstorming creativo?
4. Menciona un caso concreto de tu trabajo (RECA, RL9, inteligencia financiera) donde el tamaño de contexto podría ser un problema real.
5. ¿Qué diferencia notaste en el ejercicio de tokens entre español e inglés?

**Checklist de aprobación del día:**
- [ ] Puedo explicar tokens sin usar la palabra "palabra" como sinónimo
- [ ] Entiendo por qué un documento muy largo puede generar respuestas de peor calidad
- [ ] Hice el ejercicio de conteo de tokens con al menos 2 frases
- [ ] Escribí las 5 respuestas en Notion

---

**Mañana (Día 2):** cómo el modelo genera texto palabra por palabra (probabilidad y sampling) y qué son los embeddings.
