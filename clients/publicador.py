import paho.mqtt.client as mqtt

# Crear el cliente de MQTT
client = mqtt.Client("Publicador")

# Conectar al broker personalizado en localhost:1883
client.connect("localhost", 1883)

# Publicar un mensaje
mensaje = "¡Hola desde mi propio broker MQTT!"
client.publish("prueba/mqtt", mensaje)
print(f"Mensaje enviado: {mensaje}")

# Cerrar la conexión
client.disconnect()
