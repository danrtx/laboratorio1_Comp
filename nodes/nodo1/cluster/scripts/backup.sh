#!/bin/bash
NODO=$(hostname)
FECHA=$(date '+%Y-%m-%d %H:%M:%S')
echo "========== BACKUP =========="
echo "Nodo: $NODO | Fecha: $FECHA"

echo "[1/3] Identificando archivos críticos..."
echo "  -> /var/data/db.sqlite"
echo "  -> /etc/app/config.yml"
sleep 0.3

echo "[2/3] Comprimiendo archivos..."
echo "  -> backup_${NODO}.tar.gz generado (simulado)"
sleep 0.3

echo "[3/3] Verificando integridad del backup..."
echo "  -> Checksum OK"
echo "========== BACKUP COMPLETADO en $NODO =========="