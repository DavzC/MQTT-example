import paho.mqtt.client as mqtt

# Configuración del broker y puerto
broker = "10.43.100.217"  # Cambia a la IP del broker si es necesario
puerto = 1883

# Crear el cliente MQTT
client = mqtt.Client("ServidorCentral")

# Definir la función que se llama al recibir un mensaje
def on_message(client, userdata, message):
    print(f"Mensaje recibido en {message.topic}: {message.payload.decode()}")

# Configurar el evento de mensaje
client.on_message = on_message

# Conectar al broker
client.connect(broker, puerto)
print("Conectado al broker en", broker)

# Suscribirse a los temas de temperatura y alerta
client.subscribe("edificio/temperatura", qos=1)
client.subscribe("edificio/alerta", qos=1)
print("Escuchando en los temas 'edificio/temperatura' y 'edificio/alerta'...")

# Iniciar el bucle de escucha
client.loop_forever()
