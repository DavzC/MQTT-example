# Proyecto MQTT 

Este proyecto implementa un sistema MQTT distribuido con un broker principal y uno de respaldo, junto con un cliente suscriptor y un publicador, que se reconectan automáticamente en caso de fallo.

## Estructura del Proyecto

- `brokers/`: Contiene los scripts para el broker principal y el de respaldo.
- `clients/`: Contiene los scripts para el suscriptor y el publicador.
- `requirements.txt`: Lista de dependencias necesarias para el proyecto.

## Instalación

1. Clona el repositorio:
   
   ```bash
   git clone https://github.com/tuusuario/mqtt_failover_project.git
   cd mqtt_failover_project

2. Instala las dependencias:
   
   ```bash
   
    pip install -r requirements.txt
   
3. Ejecuta los scripts en diferentes terminales:
4. Ejecuta el broker principal:
   
   ```bash
   python brokers/BrokerP.py
   ```

5. Ejecuta el broker de respaldo:
   
   ```bash
    python brokers/BrokerR.py
    ```
   
6. Ejecuta el suscriptor:
   
   ```bash
   python clients/Subscriber.py
   ```
7. Ejecuta el publicador:
   
   ```bash
   python clients/Publisher.py
   ```
   
## Uso

Una vez ejecutados los scripts, el publicador enviará mensajes al broker principal, el cual los reenviará al suscriptor. Si el broker principal falla, el suscriptor se reconectará automáticamente al broker de respaldo y seguirá recibiendo los mensajes.

## Contribuciones

Si deseas contribuir al proyecto, por favor crea un *pull request* con tus sugerencias.

## Licencia

Distribuido bajo la licencia MIT. Ver `LICENSE` para más información.


