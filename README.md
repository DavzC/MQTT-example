# Proyecto de Monitoreo de Temperatura con MQTT y Failover

Este proyecto simula un sistema de monitoreo de temperatura en tiempo real para edificios inteligentes. Utiliza el protocolo MQTT para comunicar los datos de un sensor de temperatura hacia un servidor central a través de un broker MQTT. En caso de fallo, el servidor puede recibir alertas y datos de temperatura con configuración de failover.

## Estructura del Proyecto

La estructura de archivos del proyecto es la siguiente:

```plaintext
MQTT-example/              
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

## Autor

**David Santiago Ortiz Calderon**  

[LinkedIn](https://www.linkedin.com/in/david-ortiz-b2136a1ba/) | [GitHub](https://github.com/DavzC) 

Este proyecto fue creado para demostrar la implementación de un sistema de monitoreo IoT con MQTT, incluyendo failover y manejo de desconexiones para mejorar la resiliencia y continuidad de la comunicación en dispositivos conectados.


## Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes, por favor, abre un issue primero para discutir qué te gustaría cambiar.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
```

