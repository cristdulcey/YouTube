import azure.functions as func
import json
import logging
from .redis_service import RedisService

redis_service = RedisService()


async def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        #Obtener datos del request
        req_body = req.get_json()
        channel = req_body.get('channel', 'default-channel')
        message = req_body.get('message')
        if not message:
            return func.HttpResponse(
                "El mensaje es requerido",
                status_code=400
            )
        #Publicar notificación
        notification = {
            'type': 'notification',
            'content': message,
            'metadata': req_body.get('metadata', {})
        }
        success = redis_service.publish_notification(channel, notification)
        if success:
            return func.HttpResponse(
                json.dumps({
                    "status": "success",
                    "message": "Notificación enviada",
                    "channel": channel
                }),
                mimetype="application/json"
            )
        else:
            return func.HttpResponse(
                "Error al enviar la notificación",
                status_code=500
            )

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(
            f"Error: {str(e)}",
            status_code=500
        )
