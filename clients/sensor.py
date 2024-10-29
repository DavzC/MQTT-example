import paho.mqtt.client as mqtt
import random
import time

# Definir el broker y el puerto
broker = "ip_del_broker"
puerto = 1883

# Crear el cliente MQTT
client = mqtt.Client("SensorTemperatura")

# Configurar LWT (Last Will and Testament) para notificar desconexión inesperada
client.will_set("edificio/alerta", "Sensor de temperatura desconectado inesperadamente", qos=1, retain=True)

# Conectar al broker
client.connect(broker, puerto)
print("Conectado al broker en", broker)

# Función para enviar lecturas de temperatura
def publicar_temperatura():
    while True:
        # Simular una lectura de temperatura
        temperatura = round(random.uniform(20.0, 30.0), 2)
        print(f"Temperatura actual: {temperatura} °C")

        # Publicar en el tema con QoS 1 y mensaje retenido
        client.publish("edificio/temperatura", f"Temperatura: {temperatura} °C", qos=1, retain=True)

        # Esperar 5 segundos antes de la siguiente lectura
        time.sleep(5)

# Ejecutar la función de publicación
if __name__ == '__main__':
    publicar_temperatura()
