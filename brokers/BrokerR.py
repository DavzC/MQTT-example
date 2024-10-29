
from hbmqtt.broker import Broker
import asyncio


broker_respaldo_config = {
    'listeners': {
        'default': {
            'type': 'tcp',
            'bind': '127.0.0.1:1884'
        }
    },
    'sys_interval': 10,
    'topic-check': {
        'enabled': True,
        'plugins': ['hbmqtt.plugins.topic_taboo.TopicTabooPlugin']
    }
}

# Función principal para iniciar el broker de respaldo
async def iniciar_broker_respaldo():
    broker = Broker(broker_respaldo_config)
    await broker.start()

# Ejecutar el broker de respaldo
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(iniciar_broker_respaldo())
    loop.run_forever()
