from hbmqtt.broker import Broker
import asyncio

broker_config = {
    'listeners': {
        'default': {
            'type': 'tcp',
            'bind': 'ip_del_broker:1883'
        }
    },
    'sys_interval': 10,
    'topic-check': {
        'enabled': True
    }
}

async def iniciar_broker():
    broker = Broker(broker_config)
    await broker.start()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(iniciar_broker())
    loop.run_forever()
