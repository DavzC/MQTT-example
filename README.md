# Proyecto de Monitoreo de Temperatura con MQTT y Failover

Este proyecto simula un sistema de monitoreo de temperatura en tiempo real para edificios inteligentes. Utiliza el protocolo MQTT para comunicar los datos de un sensor de temperatura hacia un servidor central a través de un broker MQTT. En caso de fallo, el servidor puede recibir alertas y datos de temperatura con configuración de failover.

## Estructura del Proyecto

La estructura de archivos del proyecto es la siguiente:

```plaintext
MQTT-example/
├── brokers/
│   ├── brokerP.py                # Broker principal ejecutado 
├── clients/
│   ├── sensor.py                 # Cliente que simula el sensor de temperatura 
│   ├── server.py               # Servidor que recibe los datos 
├── requirements.txt              # Lista de dependencias
└── README.md                     # Documentación del proyecto
```

## Instalación

Para instalar las dependencias del proyecto, se puede utilizar el archivo `requirements.txt` con el siguiente comando:

```bash
pip install -r requirements.txt
```

## Uso

Para ejecutar el proyecto, se deben seguir los siguientes pasos:

1. Ejecutar el broker principal en la VM 1:

```bash
python brokers/brokerP.py
```

2. Ejecutar el servidor en la VM 1:

```bash
python clients/server.py
```

3. Ejecutar el sensor en la VM 2:

```bash
python clients/sensor.py
```

## Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes, por favor, abre un issue primero para discutir qué te gustaría cambiar.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
```

## Autor

- [David Ortiz]

