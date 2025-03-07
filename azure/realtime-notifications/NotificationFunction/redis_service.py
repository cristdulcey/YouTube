import redis
import json
import logging
from datetime import datetime
from typing import Dict, Any
import os


class RedisService:
    def __init__(self):
        self.redis_client = redis.Redis(
            host=os.environ["REDIS_HOST"],
            port=int(os.environ["REDIS_PORT"]),
            password=os.environ["REDIS_PASSWORD"] if "REDIS_PASSWORD" in os.environ else None,
            ssl=os.environ["REDIS_SSL"] == "True",
            decode_responses=True,
        )

    def publish_notification(self, channel: str, message: Dict[str, Any]) -> bool:
        try:
            message_with_timestamp = {
                **message,
                "timestamp": datetime.utcnow().isoformat()
            }
            result = self.redis_client.publish(
                channel,
                json.dumps(message_with_timestamp)
            )
            logging.info(f"Mensaje publicado en {channel}: {message_with_timestamp}")
            return True
        except Exception as e:
            logging.error(f"Error publicando mensaje: {str(e)}")
            return False

    def subscribe_to_channel(self, channel: str):
        pubsub = self.redis_client.pubsub()
        pubsub.subscribe(channel)
        return pubsub

    def get_message_count(self, channel: str) -> int:
        return self.redis_client.pubsub_numsub(channel)