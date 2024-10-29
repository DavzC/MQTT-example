
from hbmqtt.broker import Broker
import asyncio

# Configuración básica del broker MQTT
broker_config = {
    'listeners': {
        'default': {
            'type': 'tcp',
            'bind': '127.0.0.1:1883'
        }
    },
    'sys_interval': 10,
    'topic-check': {
        'enabled': True,
        'plugins': ['hbmqtt.plugins.topic_taboo.TopicTabooPlugin']
    }
}

# Función principal para iniciar el broker
async def iniciar_broker():
    broker = Broker(broker_config)
    await broker.start()

# Ejecutar el broker
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(iniciar_broker())
    loop.run_forever()
