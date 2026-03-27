#!/bin/bash
NODO=$(hostname)
echo "========== UPDATE =========="
echo "Nodo: $NODO"

echo "[1/3] Verificando conexión a repositorios..."
sleep 0.3

echo "[2/3] Buscando paquetes desactualizados..."
echo "  -> libssl: 1.1.0 -> 1.1.1"
echo "  -> curl: 7.81 -> 7.88"
sleep 0.3

echo "[3/3] Aplicando actualizaciones (simulado)..."
echo "  -> Paquetes actualizados correctamente"
echo "========== UPDATE COMPLETADO en $NODO =========="