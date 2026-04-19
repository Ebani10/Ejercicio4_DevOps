#!/bin/bash
# Ir a la carpeta donde están los archivos
cd /var/www/html/
# Ejecutar el script de Python para generar el resultado.txt localmente
python3 procesar.py
# Asegurar permisos para que Apache pueda leerlo
chown ec2-user:apache /var/www/html/resultado.txt
chmod 644 /var/www/html/resultado.txt