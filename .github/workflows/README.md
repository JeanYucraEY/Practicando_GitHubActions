# 📁 GitHub Actions Workflows - Referencia

Este directorio contiene todos los archivos de workflow para GitHub Actions.

## 📋 Workflows Disponibles

### 01-hello-world.yml
**Nivel**: 🟢 Básico  
**Tiempo**: ~30 segundos  
**Triggers**: push (main/develop), PR (main), manual

**Qué hace**:
- Descarga el repositorio
- Ejecuta comandos bash simples
- Muestra información del sistema
- Demuestra condicionales

**Ideal para**: Entender los conceptos básicos de workflows

```bash
# Triggers
git push origin main
git push origin develop
# O ejecuta manualmente desde Actions tab
```

---

### 02-python-tests.yml
**Nivel**: 🟡 Intermedio  
**Tiempo**: ~2 minutos  
**Triggers**: push (main), PR (main), manual

**Qué hace**:
- Configura Python 3.9, 3.10, 3.11 en paralelo
- Instala dependencias
- Ejecuta pruebas con pytest
- Genera reportes de cobertura

**Ideal para**: Aprender matrices y testing

```bash
# Todos los tests se ejecutan en paralelo
# Resultado: 1 job con 3 subprocesos simultáneos
```

---

### 03-multi-job.yml
**Nivel**: 🟡 Intermedio  
**Tiempo**: ~3-5 minutos  
**Triggers**: push (main), manual

**Qué hace**:
- BUILD: Compila la aplicación
- TEST: Ejecuta tests (espera a BUILD)
- DEPLOY: Despliega (solo en main)
- NOTIFY: Notifica resultado (siempre)

**Ideal para**: Entender dependencias entre jobs y artefactos

```
BUILD (30s)
  ↓ (necesita)
TEST (1m)
  ↓ (necesita)
DEPLOY (1m, solo si main)
  ↓ (siempre ejecuta)
NOTIFY (10s)
```

---

### 04-scheduled.yml
**Nivel**: 🟡 Intermedio  
**Tiempo**: ~1 minuto  
**Triggers**: schedule (cada día 10:00 UTC), manual

**Qué hace**:
- Se ejecuta diariamente automáticamente
- Verifica estado del repositorio
- Ejecuta tareas de mantenimiento

**Ideal para**: Aprender cron schedules y tareas automáticas

```yaml
# Cron: 0 10 * * * = Cada día a las 10:00 UTC
# Personaliza el horario según tu zona horaria
```

---

### 05-on-pull-request.yml
**Nivel**: 🟡 Intermedio  
**Tiempo**: ~1 minuto  
**Triggers**: PR opened/updated/reopened

**Qué hace**:
- Obtiene información del PR
- Muestra archivos modificados
- Valida cambios (busca TODO/FIXME)
- Agrega comentario automático

**Ideal para**: Aprender eventos de PR y GitHub API

```bash
# Se ejecuta automáticamente cuando:
git push origin feature-branch
# y luego creas PR en GitHub
```

---

### 06-with-environment-variables.yml
**Nivel**: 🟡 Intermedio  
**Tiempo**: ~30 segundos  
**Triggers**: push (main), manual (con inputs)

**Qué hace**:
- Demuestra variables globales
- Variables del job
- Variables del step
- Inputs interactivos
- Uso de secretos

**Ideal para**: Entender variables de entorno y inputs

```yaml
# Inputs disponibles:
# - environment: development|staging|production
# - log_level: debug|info|warning|error
```

---

### 07-code-quality.yml
**Nivel**: 🔴 Avanzado  
**Tiempo**: ~2 minutos  
**Triggers**: push (main/develop), PR (main), manual

**Qué hace**:
- Black: Formatea código
- Flake8: Valida sintaxis
- Pylint: Verifica calidad
- MyPy: Validación de tipos

**Ideal para**: Aprender verificación de calidad de código

```bash
# Herramientas usadas:
pip install black flake8 pylint mypy
```

---

## 🎯 Camino de Aprendizaje Sugerido

```
Principiante
    ↓
1️⃣ 01-hello-world.yml
    ↓ (Entiendes: on, jobs, steps, run)
2️⃣ 06-with-environment-variables.yml
    ↓ (Entiendes: env, variables, inputs)
3️⃣ 02-python-tests.yml
    ↓ (Entiendes: matrix, actions, setup)

Intermedio
    ↓
4️⃣ 05-on-pull-request.yml
    ↓ (Entiendes: pull_request event, github api)
5️⃣ 04-scheduled.yml
    ↓ (Entiendes: schedule, cron)
6️⃣ 03-multi-job.yml
    ↓ (Entiendes: needs, artefactos, condicionales)

Avanzado
    ↓
7️⃣ 07-code-quality.yml
    ↓ (Entiendes: múltiples herramientas, linting)
```

---

## ✅ Checklist: ¿Qué Debo Saber?

Después de estudiar estos workflows, deberías entender:

### Básico
- [ ] Estructura de un workflow YAML
- [ ] Qué es un job y un step
- [ ] Cómo se disparan los workflows
- [ ] Comandos básicos con `run:`

### Intermedio
- [ ] Variables de entorno (env)
- [ ] Acciones predefinidas (actions/*)
- [ ] Matrices de testing
- [ ] Dependencias entre jobs (needs)
- [ ] Condicionales (if)
- [ ] Eventos de PR

### Avanzado
- [ ] Intercambio de artefactos
- [ ] GitHub API con github-script
- [ ] Schedules con cron
- [ ] Secretos y seguridad
- [ ] Contextos de ejecución

---

## 🔨 Modificar Workflows

Para practicar, intenta:

1. **Cambiar triggers** en 01-hello-world.yml
2. **Agregar más herramientas** a 07-code-quality.yml
3. **Crear tu propio workflow** basado en 06-with-environment-variables.yml
4. **Agregar un nuevo job** a 03-multi-job.yml

---

## 📚 Recursos Adicionales

- [README.md](../README.md) - Guía principal
- [SETUP.md](../SETUP.md) - Configuración inicial
- [CHEAT_SHEET.md](../CHEAT_SHEET.md) - Referencia rápida
- [WORKFLOW_DIAGRAMS.md](../WORKFLOW_DIAGRAMS.md) - Gráficos explicativos
- [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) - Solución de errores

---

**¿Listo para dominar GitHub Actions? ¡Comienza con 01-hello-world.yml!** 🚀
