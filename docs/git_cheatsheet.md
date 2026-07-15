# 🔧 Git Cheatsheet — Reto 30 Días

## Configuración inicial (una sola vez)
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"
```

## Conectar carpeta local con GitHub (una sola vez, al inicio)
```bash
git init
git add .
git commit -m "Día 0: estructura inicial del repositorio y plan de 30 días"
git branch -M main
git remote add origin https://github.com/tu-usuario/tu-repo.git
git push -u origin main
```

## Rutina diaria (cada noche, después de estudiar)
```bash
git add .
git commit -m "Día X: [tema del día]"
git push
```

## Revisar progreso
```bash
git status          # archivos modificados/nuevos aún no confirmados
git log --oneline   # historial resumido de commits
git diff            # ver cambios exactos línea por línea
```

## Si algo sale mal
```bash
git reset --soft HEAD~1   # deshace el último commit, pero conserva los cambios
git checkout -- archivo   # descarta cambios locales de un archivo específico
```

## Buenas prácticas de mensajes de commit
- Empieza siempre con "Día X:" para que el historial sea cronológicamente legible
- Sé específico: "Día 5: agrego evaluación de prompts con few-shot" (bien) vs "cambios" (mal)
- Un commit = un avance coherente, no mezcles temas de días distintos en un solo commit
