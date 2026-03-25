# Guía de Configuración Inicial

Este archivo te guía a través de los primeros pasos para configurar el repositorio.

## 1️⃣ Configuración del Repositorio

### A. Configurar git (si es primera vez)
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@ejemplo.com"
```

### B. Verificar remoto
```bash
git remote -v
# Deberías ver origin apuntando a tu repositorio
```

## 2️⃣ Configuración Local

### A. Crear ambiente virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python -m venv venv
source venv/bin/activate
```

### B. Instalar dependencias
```bash
pip install -r requirements-dev.txt
```

### C. Verificar instalación
```bash
python --version
pytest --version
```

## 3️⃣ Ejecutar Workflows Localmente

### Primer Test
```bash
# Ejecutar las pruebas
pytest tests/ -v

# Con cobertura
pytest tests/ --cov=src --cov-report=term-missing
```

### Demo Script
```bash
# En Windows (necesitas Git Bash o WSL)
bash scripts/demo.sh

# O simplemente con Python
python -c "import os; os.system('ls -la')"
```

## 4️⃣ Hacer tu Primer Push

```bash
# Ver estado
git status

# Agregar cambios
git add .

# Commit
git commit -m "Configuración inicial de workflows"

# Push
git push origin main
```

## 5️⃣ Ver Workflows en Acción

1. Ve a https://github.com/TU_USUARIO/Practicando_GitHubActions/actions
2. Verás que tus workflows se ejecutaron
3. Haz clic en uno para ver los detalles

## 🎯 Checklist de Configuración

- [ ] Repositorio clonado
- [ ] Git configurado
- [ ] Python virtual env creado
- [ ] Dependencias instaladas
- [ ] Pruebas ejecutadas localmente
- [ ] Primer push realizado
- [ ] Workflows visibles en GitHub

---

**¡Ahora estás listo para practicar GitHub Actions!** 🚀
