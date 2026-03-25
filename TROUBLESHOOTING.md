# 📖 Errores Comunes y Soluciones

Aquí encontrarás soluciones a problemas frecuentes al trabajar con GitHub Actions.

## ❌ Error: "Runner offline" o "No runners available"

**Causa**: No hay runners disponibles para ejecutar el workflow.

**Solución**:
- Verifica que uses `runs-on: ubuntu-latest` (está disponible por defecto)
- Si usaste `runs-on: self-hosted`, asegúrate de tener un runner configurado

## ❌ Error: "Permission denied" en scripts

**Causa**: El archivo no tiene permisos de ejecución.

**Solución**:
```bash
# Dar permisos de ejecución localmente
chmod +x scripts/demo.sh

# Luego en el workflow, usa bash explícitamente
run: bash scripts/demo.sh
```

## ❌ Error: "Python not found"

**Causa**: Python no está instalado en el runner.

**Solución**:
```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # Agregacorporate el setup de Python
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
```

## ❌ Error: "Workflow file not found"

**Causa**: El archivo YAML está en la ubicación incorrecta.

**Solución**:
- Los workflows DEBEN estar en `.github/workflows/`
- El nombre debe terminar en `.yml` o `.yaml`
- Ruta correcta: `.github/workflows/nombre.yml`

## ❌ Error: "Syntax error in workflow file"

**Causa**: El YAML tiene errores de indentación o sintaxis.

**Solución**:
- Verifica la indentación (usa 2 espacios, NO tabs)
- Usa [Validador Online](https://rhysd.github.io/actionlint/)
- En VS Code, instala la extensión "YAML"

## ❌ Error: "GitHub Script fails"

**Causa**: Problemas con GitHub API GraphQL.

**Solución**:
```yaml
- uses: actions/github-script@v7
  with:
    # Asegúrate de usar 'this.context' o 'github'
    script: |
      console.log(context.payload)
```

## ⚠️ Advertencia: "Checkout action version 3 is deprecated"

**Solución**:
```yaml
# Usa la versión 4
- uses: actions/checkout@v4
```

## 🔍 Cómo Debuggear

### Activar Debug Logging
```yaml
- name: Enable debug logging
  run: echo "::debug::This is a debug message"
```

### Ver Variables de Contexto
```yaml
- name: Print context
  run: |
    echo "Event: ${{ github.event_name }}"
    echo "Actor: ${{ github.actor }}"
    echo "Branch: ${{ github.ref_name }}"
```

### Ver Outputs de Steps
```yaml
- id: my-step
  run: echo "output-value=test" >> $GITHUB_OUTPUT

- name: Use output
  run: echo "The output was: ${{ steps.my-step.outputs.output-value }}"
```

---

¿Más problemas? Consulta la [documentación oficial](https://docs.github.com/en/actions).
