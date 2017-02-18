
# testVelocidad

Script para la comprobación periódica de la velocidad de conexión a Internet y la generación de informes estadísticos de resultados.

Más **información** (pendiente de publicar un artículo sobre la herramienta aquí mostrada) en el [Informático de Guardia](https://andalinux.wordpress.com)

## Instalación

Instala las dependencias recogidas en el fichero [dependencias.lst](https://github.com/jasvazquez/testVelocidad/blob/master/dependencias.lst) mediante un

> pip install -r dependencias.lst

## Uso

Aunque el script se puede utilizar desde la terminal de comandos (```python testVelocidad.py --help``` para más información de los parámetros actualmente permitidos) se aconseja programar su uso mediante _tareas cron_. Sirva de ejemplo el siguiente fragmento:

> #minute	hour	mday	month	wday	who	command
> 0	*	*	*	*	root	source /home/MIUSUARIO/scripts/testVelocidad/bin/activate && python /home/MIUSUARIO/scripts/testVelocidad/testVelocidad.py -m

En el que se solicita, cada hora, que se realice (y anote para su uso posterior) una nueva medición de la velocidad (parámetro -m)

En el ejemplo:
1. Se hace uso de los entornos virtuales de Python (_source /home/MIUSUARIO/scripts/testVelocidad/bin/activate_)
1. El directorio en el que se ha colocado el script es _/home/MIUSUARIO/scripts/testVelocidad_
1. Debes sustituir MIUSUARIO por tu nombre de usuario "Linux" y/o adaptar la ruta absoluta (cron no "entiende" de rutas relativas) a la ubicación en la que tengas el código del script

Si te surgen dudas sobre su uso, ponte en contacto conmigo a través d[el soporte técnico del Informático de Guardia](https://andalinux.wordpress.com/about)
