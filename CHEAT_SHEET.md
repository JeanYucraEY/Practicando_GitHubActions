# 🎯 GitHub Actions - Cheat Sheet (Hoja de Referencia Rápida)

## Estructura Básica

```yaml
name: Nombre del Workflow

on:
  push:
    branches: [ main ]

jobs:
  nombre-job:
    runs-on: ubuntu-latest
    steps:
      - name: Descripción del step
        run: comando
```

---

## Eventos (WHEN)

```yaml
on:
  # Cuando hay push a rama específica
  push:
    branches: [ main, develop ]
  
  # Cuando se abre/actualiza PR
  pull_request:
    branches: [ main ]
  
  # Ejecución programada (cron)
  schedule:
    - cron: '0 10 * * *'
  
  # Ejecución manual
  workflow_dispatch:
  
  # Otros eventos
  release:
    types: [published]
  workflow_call:  # Llamada desde otro workflow
```

---

## Runners (DÓNDE)

```yaml
runs-on: ubuntu-latest      # Linux (recomendado)
runs-on: windows-latest     # Windows
runs-on: macos-latest       # macOS
runs-on: self-hosted        # Tu propio servidor
```

---

## Actions Comunes (HERRAMIENTAS)

```yaml
# Descargar el código
- uses: actions/checkout@v4

# Configurar Python
- uses: actions/setup-python@v4
  with:
    python-version: '3.11'

# Configurar Node.js
- uses: actions/setup-node@v4
  with:
    node-version: '18'

# Subir archivos entre jobs
- uses: actions/upload-artifact@v3
  with:
    name: my-artifact
    path: ./dist

# Descargar artefactos
- uses: actions/download-artifact@v3
  with:
    name: my-artifact

# Usar GitHub API
- uses: actions/github-script@v7
  with:
    script: |
      console.log(context.payload)

# Codecov
- uses: codecov/codecov-action@v3

# Publicar en GitHub Pages
- uses: actions/deploy-pages@v2
```

---

## Comandos (RUN)

```yaml
# Comando simple
- run: echo "Hola mundo"

# Múltiples líneas
- run: |
  npm install
  npm run build
  npm test

# Con condicional
- if: success()
  run: echo "Todo OK"

- if: failure()
  run: echo "Algo falló"

- if: github.ref == 'refs/heads/main'
  run: npm run deploy
```

---

## Variables de Contexto

```yaml
# Información del repositorio
${{ github.repository }}        # owner/name
${{ github.ref_name }}          # rama (main, develop)
${{ github.sha }}               # último commit
${{ github.workflow }}          # nombre del workflow

# Información del evento
${{ github.event_name }}        # push, pull_request, etc
${{ github.actor }}             # usuario que disparó
${{ github.event.number }}      # PR number

# Pull Request específico
${{ github.event.pull_request.title }}
${{ github.event.pull_request.body }}
${{ github.event.pull_request.user.login }}

# Rutas
${{ github.workspace }}         # carpeta raíz (/home/runner/work)
${{ github.action_path }}       # carpeta de la action

# Estados
${{ job.status }}               # success, failure
```

---

## Matrices (TESTING EN MÚLTIPLES VERSIONES)

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.9', '3.10', '3.11']
        os: [ubuntu-latest, windows-latest]
    
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      
      - run: pytest tests/
```

---

## Dependencias Entre Jobs

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # ...

  test:
    runs-on: ubuntu-latest
    needs: build  # Espera a que build termine
    steps:
      # ...

  deploy:
    runs-on: ubuntu-latest
    needs: [build, test]  # Espera a ambos
    if: success()  # Solo si ambos éxito
    steps:
      # ...
```

---

## Variables de Entorno

```yaml
# Global
env:
  VERSION: 1.0.0

# En job
jobs:
  my-job:
    env:
      DEBUG: true
    steps:
      # Step
      - run: echo ${{ env.VERSION }}

# En step
- name: My step
  env:
    LOCAL_VAR: local_value
  run: echo "LOCAL_VAR=$LOCAL_VAR"
```

---

## Secretos (INFORMACIÓN SENSIBLE)

```yaml
# Definir en GitHub:
# Settings → Secrets and variables → Actions → New repository secret

# Usar en workflow:
- name: Deploy
  env:
    API_KEY: ${{ secrets.API_KEY }}
    DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
  run: |
    # Usar $API_KEY
    # NUNCA imprimir en logs!

# Inputs para workflow_dispatch con secretos
env:
  TOKEN: ${{ secrets.GITHUB_TOKEN }}  # Automático
```

---

## Condicionales

```yaml
# Si-entonces
- if: github.ref == 'refs/heads/main'
  run: echo "Es main"

# Comprobar evento
- if: github.event_name == 'pull_request'
  run: echo "Es un PR"

# Status de job anterior
- if: success()
  run: echo "OK"

- if: failure()
  run: echo "Falló"

- if: always()
  run: echo "Siempre ejecutar"

# Comprobar archivo cambiado
- if: contains(github.event.head_commit.modified, 'package.json')
  run: npm install
```

---

## Outputs (COMPARTIR DATOS)

```yaml
# En un step
- id: my-step
  run: echo "output-name=value123" >> $GITHUB_OUTPUT

# Usar el output
- name: Use output
  run: echo "${{ steps.my-step.outputs.output-name }}"

# Entre jobs (requiere upload/download de artefactos)
- uses: actions/upload-artifact@v3
  with:
    name: data
    path: output.json

- uses: actions/download-artifact@v3
  with:
    name: data
```

---

## Ejemplos Rápidos

### ✅ Deploy a Vercel
```yaml
- name: Deploy to Vercel
  env:
    VERCEL_TOKEN: ${{ secrets.VERCEL_TOKEN }}
  run: |
    npm install -g vercel
    vercel --prod --token $VERCEL_TOKEN
```

### ✅ Enviar Slack Notification
```yaml
- name: Slack Notification
  if: always()
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    text: 'Build ${{ job.status }}'
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

### ✅ Crear Release
```yaml
- name: Create Release
  uses: actions/create-release@v1
  with:
    tag_name: v1.0.0
    release_name: Release v1.0.0
    body: Changelog aquí
```

### ✅ Cache de Dependencias
```yaml
- uses: actions/cache@v3
  with:
    path: ~/.pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

---

## Debugging

```yaml
# Activar debug logging
env:
  RUNNER_DEBUG: 1

# Imprimir contexto
- name: Debug
  run: |
    echo "Branch: ${{ github.ref_name }}"
    echo "Event: ${{ github.event_name }}"
    echo "Actor: ${{ github.actor }}"
    echo "Repo: ${{ github.repository }}"
```

---

## Validación de YAML

```bash
# Online: https://rhysd.github.io/actionlint/
# CLI: actionlint .github/workflows/
```

---

**¡Imprime este cheat sheet y úsalo como referencia!** 📌
