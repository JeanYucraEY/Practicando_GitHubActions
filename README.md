# 📚 Practicando GitHub Actions

Un repositorio educativo para aprender y practicar **GitHub Actions** con ejemplos reales y documentación completa.

## 🎯 Objetivo

Este repositorio contiene una serie de workflows de ejemplo que demuestran las capacidades principales de GitHub Actions, desde lo básico hasta casos de uso más complejos.

## 📁 Estructura del Proyecto

```
Practicando_GitHubActions/
├── .github/
│   └── workflows/
│       ├── 01-hello-world.yml              # Workflow básico
│       ├── 02-python-tests.yml             # Workflow con pruebas
│       ├── 03-multi-job.yml                # Workflow con múltiples jobs
│       ├── 04-scheduled.yml                # Workflow programado
│       ├── 05-on-pull-request.yml          # Workflow en PR
│       └── 06-with-environment-variables.yml # Variables de entorno
├── src/
│   ├── __init__.py
│   └── calculadora.py                      # Código de ejemplo
├── tests/
│   ├── __init__.py
│   └── test_calculadora.py                 # Pruebas de ejemplo
├── scripts/
│   └── demo.sh                             # Script de demostración
├── requirements.txt                        # Dependencias
├── requirements-dev.txt                    # Dependencias de desarrollo
├── pytest.ini                              # Configuración de pytest
└── README.md                               # Este archivo
```

## 🚀 Workflows Disponibles

### 1️⃣ **01-hello-world.yml** - Hello World Workflow
El workflow más básico que aprenderás.

**Características:**
- Se ejecuta en: `push` y `pull_request`
- Muestra comandos básicos de bash
- Demuestra condicionales
- Permite ejecución manual (`workflow_dispatch`)

---

### 2️⃣ **02-python-tests.yml** - Python Tests
Ejecuta pruebas en múltiples versiones de Python.

**Características:**
- Usa `matrix` para probar en Python 3.9, 3.10 y 3.11
- Instala dependencias con pip
- Ejecuta pruebas con pytest
- Genera reportes de cobertura

---

### 3️⃣ **03-multi-job.yml** - Multi-Job Workflow
Demuestra jobs que dependen unos de otros.

**Características:**
- 4 jobs diferentes: build, test, deploy, notify
- Usa `needs` para establecer dependencias
- Intercambia artefactos entre jobs
- Condicionales en jobs

---

### 4️⃣ **04-scheduled.yml** - Scheduled Workflow
Ejecuta un workflow en un horario específico.

**Características:**
- Cron schedule: `0 10 * * *` (Diariamente a las 10:00 UTC)
- Ejecución manual con `workflow_dispatch`
- Ideal para tareas de mantenimiento

---

### 5️⃣ **05-on-pull-request.yml** - Pull Request Workflow
Análisis automático en Pull Requests.

**Características:**
- Obtiene información del PR
- Muestra archivos modificados
- Valida cambios
- Agrega comentarios automáticos

---

### 6️⃣ **06-with-environment-variables.yml** - Environment Variables
Demuestra uso de variables en workflows.

**Características:**
- Variables globales de workflow
- Variables del job
- Variables del step
- Inputs interactivos

---

## 🛠️ Cómo Usar Este Repositorio

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tuusuario/Practicando_GitHubActions.git
cd Practicando_GitHubActions
```

### 2. Configurar Ambiente Local

#### Con Python venv:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python -m venv venv
source venv/bin/activate
```

#### Instalar dependencias:
```bash
pip install -r requirements-dev.txt
```

### 3. Ejecutar Pruebas Localmente
```bash
pytest tests/ -v
```

### 4. Hacer tu Primer Push
```bash
git add .
git commit -m "Configuración inicial"
git push origin main
```

### 5. Ver Workflows en Acción
1. Ve a https://github.com/TU_USUARIO/Practicando_GitHubActions/actions
2. Verás tus workflows ejecutándose
3. Haz clic para ver detalles

---

## 📚 Documentación Adicional

- 📖 [SETUP.md](SETUP.md) - Guía de configuración inicial
- 🔧 [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Errores comunes y soluciones
- 📝 [Documentación oficial de GitHub Actions](https://docs.github.com/en/actions)

---

## 🎓 Conceptos Clave

✅ **Básicos**: on, jobs, steps, runs-on  
✅ **Eventos**: push, pull_request, schedule, workflow_dispatch  
✅ **Acciones**: checkout, setup-python, upload-artifact, github-script  
✅ **Avanzado**: matrix, dependencias, condicionales, variables, secretos  

---

## 🤝 Próximos Pasos

1. Modifica los workflows existentes
2. Crea tus propios workflows
3. Integra con servicios externos (Slack, Discord)
4. Automatiza deploys

---

**¡Feliz aprendizaje con GitHub Actions!** 🚀