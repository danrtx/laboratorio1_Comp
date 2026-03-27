#!/bin/bash
NODO=$(hostname)
echo "========== DEPLOY =========="
echo "Nodo: $NODO"
echo "[1/3] Verificando entorno..."
sleep 0.5

if [ -d "/tmp/app" ]; then
    echo "[OK] Directorio de app encontrado"
else
    mkdir -p /tmp/app
    echo "[OK] Directorio creado: /tmp/app"
fi

echo "[2/3] Copiando archivos de la aplicación..."
echo "  -> app.jar copiado"
echo "  -> config.yml copiado"
sleep 0.5

echo "[3/3] Iniciando servicio..."
echo "  -> Servicio arrancado en puerto 8080"
echo "========== DEPLOY COMPLETADO en $NODO =========="