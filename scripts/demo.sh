#!/bin/bash

# Script de ejemplo para GitHub Actions
# Este script muestra las capacidades básicas

echo "=========================================="
echo "Script de Demostración GitHub Actions"
echo "=========================================="
echo ""

# Variables
PROJECT_NAME="Practicando GitHub Actions"
CURRENT_DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "📋 Información del Proyecto:"
echo "Nombre: $PROJECT_NAME"
echo "Fecha: $CURRENT_DATE"
echo "Usuario: $(whoami)"
echo "Sistema: $(uname -s)"
echo ""

echo "📂 Estructura del Proyecto:"
echo "---"
tree -L 2 . --dirsfirst 2>/dev/null || find . -maxdepth 2 -type f -o -type d | sort | head -20
echo "---"
echo ""

echo "📊 Estadísticas del Repositorio:"
if [ -d .git ]; then
    echo "Total de commits: $(git rev-list --count HEAD 2>/dev/null || echo 'N/A')"
    echo "Ramas: $(git branch -a 2>/dev/null | wc -l)"
    echo "Último commit: $(git log -1 --format=%B 2>/dev/null || echo 'N/A')"
fi
echo ""

echo "✅ Script completado exitosamente"
