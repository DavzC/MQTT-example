import paho.mqtt.client as mqtt

# Crear el cliente de MQTT
client = mqtt.Client("Suscriptor")

# Definir la función que se llama cuando se recibe un mensaje
def on_message(client, userdata, message):
    print(f"Mensaje recibido en {message.topic}: {message.payload.decode()}")

# Configurar el evento de mensaje
client.on_message = on_message

# Conectar al broker personalizado en localhost:1883
client.connect("localhost", 1883)

# Suscribirse al tema
client.subscribe("prueba/mqtt")

# Iniciar el bucle de escucha
print("Escuchando en el tema 'prueba/mqtt'...")
client.loop_forever()
