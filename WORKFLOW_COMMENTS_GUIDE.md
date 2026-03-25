# 📝 Guía de Comentarios en Workflows

Todos los workflows han sido comentados línea por línea para facilitar tu aprendizaje. Esta guía muestra qué se explicó en cada uno.

---

## 🟢 Workflow #1: hello-world.yml (BÁSICO)

**Temas comentados:**
- ✅ Estructura básica: `name`, `on`, `jobs`
- ✅ Sección `TRIGGERS`: cuándo se dispara el workflow
  - `push` a ramas específicas
  - `pull_request` contra main
  - `workflow_dispatch` para ejecución manual
- ✅ Sección `JOBS`: qué tareas ejecutar
- ✅ Sección `STEPS`: pasos individuales en orden
- ✅ `uses:` para acciones predefinidas
- ✅ `run:` para comandos bash
- ✅ Condicionales: `if: github.event_name == 'pull_request'`
- ✅ Variables de contexto: `${{ github.event_name }}`
- ✅ Múltiples comandos con pipe `|`

**Aprenderás:** Los conceptos más básicos de GitHub Actions

---

## 🟡 Workflow #2: python-tests.yml (TESTING)

**Temas comentados:**
- ✅ `strategy.matrix`: ejecutar en múltiples versiones
  - Crear instancias paralelas del job
  - Acceder a valores de matriz: `${{ matrix.python-version }}`
- ✅ Acciones predefinidas con parámetros
  - `uses: actions/setup-python@v4`
  - `with:` para parámetros de entrada
- ✅ Instalar herramientas: pip, pytest, pytest-cov
- ✅ Ejecutar comandos complejos
- ✅ Generar reportes de cobertura (XML)
- ✅ Subir reportes a servicios externos (Codecov)
- ✅ Condicional `if: always()`: ejecutar sin importar resultado anterior

**Aprenderás:** Testing automatizado en múltiples versiones

---

## 🟡 Workflow #3: multi-job.yml (DEPENDENCIAS Y ARTEFACTOS)

**Temas comentados:**
- ✅ Múltiples jobs en el mismo workflow
- ✅ Dependencias entre jobs
  - `needs: build` - un job espera a otro
  - `needs: [build, test, deploy]` - esperar a múltiples jobs
- ✅ Compartir archivos entre jobs
  - `uses: actions/upload-artifact@v3` - guardar archivos
  - `uses: actions/download-artifact@v3` - recuperar archivos
- ✅ Condicionales en jobs
  - `if: github.ref == 'refs/heads/main'` - solo en main
  - `if: always()` - ejecutar siempre (incluso si hay errores)
- ✅ Acceder a status de jobs anteriores
  - `${{ needs.build.result }}` - ver si pasó/falló
- ✅ Flujo secuencial: BUILD → TEST → DEPLOY → NOTIFY

**Aprenderás:** Orquestar múltiples tareas complejas

---

## 🟡 Workflow #4: scheduled.yml (TAREAS PROGRAMADAS)

**Temas comentados:**
- ✅ Sintaxis CRON: formato de programación
  - `'0 10 * * *'` = cada día a las 10:00 UTC
  - Explicación de cada valor: minuto, hora, día, mes, día_semana
- ✅ Ejemplos de cron comunes
  - Cada día, cada 6 horas, lunes-viernes, etc.
- ✅ Manejo de zonas horarias
  - `$TZ` - variable de zona horaria
- ✅ Comandos git avanzados
  - `git log -1 --format=%H` - último commit hash
  - `git log -1 --format=%an` - autor del commit
  - `git log -1 --format=%s` - mensaje del commit
- ✅ Comandos útiles del sistema
  - `date` - fecha y hora actual

**Aprenderás:** Automatizar tareas recurrentes (backups, reportes, mantenimiento)

---

## 🟡 Workflow #5: on-pull-request.yml (CODE REVIEW)

**Temas comentados:**
- ✅ Eventos de Pull Request
  - `opened` - cuando se crea el PR
  - `synchronize` - cuando se agregan commits
  - `reopened` - cuando se reabre un PR cerrado
- ✅ Acceso a información del PR
  - `github.event.pull_request.number` - número del PR
  - `github.event.pull_request.title` - título
  - `github.event.pull_request.user.login` - autor
  - `github.event.pull_request.body` - descripción
- ✅ Comandos git avanzados
  - `git diff --name-only` - archivos modificados
  - `git diff --stat` - estadísticas de cambios
  - `git diff | grep -E` - buscar patrones
- ✅ Usar GitHub API desde workflows
  - `uses: actions/github-script@v7`
  - Crear comentarios automáticamente
  - Acceder a `context.issue.number`, `context.repo`
- ✅ Validaciones automáticas
  - Buscar comentarios TODO/FIXME/XXX

**Aprenderás:** Automatizar revisiones de código y feedback

---

## 🟡 Workflow #6: with-environment-variables.yml (VARIABLES Y SECRETOS)

**Temas comentados:**
- ✅ Jerarquía de variables
  - STEP level (solo en ese step)
  - JOB level (en todos los steps del job)
  - WORKFLOW level (global)
  - CONTEXT variables (información de GitHub)
- ✅ Inputs de `workflow_dispatch`
  - `type: choice` - dropdown
  - `required: true|false`
  - `default:` - valor predeterminado
  - `options:` - opciones disponibles
- ✅ Context variables útiles
  - `github.ref_name` - nombre de la rama
  - `github.workflow` - nombre del workflow
  - `github.run_id` - ID de la ejecución
  - `github.run_number` - número secuencial
- ✅ Manejo seguro de secretos
  - `${{ secrets.NOMBRE }}`
  - `${#VARIABLE}` - longitud (no el contenido)
  - ⚠️ NUNCA imprimir secretos en logs

**Aprenderás:** Configurar workflows dinámicos y seguros

---

## 🔴 Workflow #7: code-quality.yml (ANÁLISIS DE CÓDIGO)

**Temas comentados:**
- ✅ Black (formateador)
  - `black --check` - verificar sin cambios
  - Formato automático de código
- ✅ Flake8 (validador PEP8)
  - `--count` - contar errores
  - `--select=E9,F63,F7,F82` - filtrar tipos de error
  - `--show-source` - mostrar línea del error
  - `--statistics` - resumen de errores
- ✅ Pylint (análisis profundo)
  - `--fail-under=7.0` - umbral de calidad
  - Puntuación de 0 a 10
- ✅ MyPy (verificador de tipos)
  - Validar type hints
  - `--ignore-missing-imports` - ignorar imports sin tipos
- ✅ Condicional `|| true`
  - No fallar el workflow aunque haya errores
  - Análisis informativo, no bloqueante
- ✅ Mejores prácticas de calidad

**Aprenderás:** Mantener código limpio y de alta calidad

---

## 📚 Guía de Lectura Recomendada

**Para principiantes:**
1. Primero: Workflow #1 (hello-world.yml)
2. Luego: Workflow #6 (variables)
3. Después: Workflow #2 (testing)

**Para nivel intermedio:**
4. Workflow #5 (Pull Requests)
5. Workflow #4 (Scheduled tasks)
6. Workflow #3 (Multi-job)

**Para avanzado:**
7. Workflow #7 (Code quality)

---

## 🎯 Ejercicios Prácticos

### Ejercicio 1: Modificar Workflow #1
- [ ] Agrega un nuevo step que muestre variables de entorno
- [ ] Cambia el trigger para que se ejecute en `develop` también
- [ ] Agrega un condicional que se ejecute solo en push (no en PR)

### Ejercicio 2: Crear tu Propio Workflow
- [ ] Crea `08-my-workflow.yml`
- [ ] Usa al menos 3 de los conceptos aprendidos
- [ ] Agrega comentarios en cada sección

### Ejercicio 3: Combinar Conceptos
- [ ] Usa `needs` para crear dependencias
- [ ] Usa `matrix` para testing en múltiples versiones
- [ ] Crea variables globales, de job y de step

---

## 🔍 Cómo Leer los Comentarios

Cada workflow sigue este patrón:

```yaml
# Encabezado de sección
# Explicación general
section-name:
  # Comentario de subsección
  sub-item: value  # Comentario inline
  # Más explicación
```

**Consejos para aprender:**
1. Lee el encabezado del workflow
2. Lee los comentarios de cada sección
3. Ejecuta el workflow y observa los logs
4. Modifica el código y experimenta
5. Consulta la documentación oficial

---

## 📖 Links a Documentación

- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)
- [Context variables](https://docs.github.com/en/actions/learn-github-actions/contexts)
- [Variables and secrets](https://docs.github.com/en/actions/learn-github-actions/variables)

---

## ✅ Verificación de Comprensión

¿Entiendes estos conceptos?

- [ ] ¿Qué es un job?
- [ ] ¿Qué es un step?
- [ ] ¿Qué diferencia hay entre `push` y `pull_request`?
- [ ] ¿Para qué sirve `needs`?
- [ ] ¿Qué es un artefacto?
- [ ] ¿Cómo funcionan las matrices?
- [ ] ¿Cómo crear variables locales?
- [ ] ¿Por qué no debo imprimir secretos?

Si respondiste "no" a alguna, relé el workflow correspondiente. 🚀

---

**¡Los workflows comentados están listos para estudiar!** 📖
