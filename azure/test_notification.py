import requests
import time

def send_test_notifications(num_messages=1000):
    url = "http://localhost:7071/api/NotificationFunction"
    start_time = time.time()
    successful = 0
    for i in range(num_messages):
        payload = {
            "channel": "test-channel",
            "message": f"Test message {i}",
            "metadata": {
                "priority": "high",
                "test_id": i
            }
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            successful += 1
    end_time = time.time()
    duration = end_time - start_time
    print(f"""
    Resultados de la prueba:
    ----------------------
    Mensajes enviados: {num_messages}
    Mensajes exitosos: {successful}
    Tiempo total: {duration:.2f} segundos
    Mensajes por segundo: {num_messages / duration:.2f}
    """)


send_test_notifications()