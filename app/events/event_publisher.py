import aio_pika
import json
from app.logger import logger

RABBITMQ_URL = "amqp://ariel:rabbit123@3.232.44.72:5672"  

async def publish_flight_created(flight_id: int):
    try:
        connection = await aio_pika.connect_robust(RABBITMQ_URL)
        channel = await connection.channel()
        
        message_body = json.dumps({"id": flight_id}).encode("utf-8")
        
        await channel.default_exchange.publish(
            aio_pika.Message(body=message_body),
            routing_key="flight.created"
        )
        logger.info(f"📤 Evento publicado correctamente: Vuelo creado ID={flight_id}")
    
    except Exception as e:
        logger.error(f"❌ Error al publicar evento flight.created: {str(e)}")
    
    finally:
        await connection.close()
