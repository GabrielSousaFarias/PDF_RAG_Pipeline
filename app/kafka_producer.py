import json

from confluent_kafka import Producer

from app.config import settings


producer = Producer({
    "bootstrap.servers": settings.kafka_bootstrap_servers
})


def publish_pdf_uploaded_event(payload: dict) -> None:
    print(f"[PRODUCER] Sending event: {payload}")

    producer.produce(
        topic=settings.pdf_topic,
        key=payload["file_id"],
        value=json.dumps(payload).encode("utf-8")
    )

    producer.flush()

    print("[PRODUCER] Event sent successfully")