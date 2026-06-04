import json
from confluent_kafka import Consumer
from app.config import settings
from worker.pdf_parser import parse_pdf, save_result

consumer = Consumer({
    "bootstrap.servers": settings.kafka_bootstrap_servers,
    "group.id": "pdf-parser-worker",
    "auto.offset.reset": "earliest"
})

consumer.subscribe([settings.pdf_topic])

print("Waiting for messages...")

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(msg.error())
        continue
    event = json.loads(
        msg.value().decode("utf-8")
    )
    print(event)
    file_id = event["file_id"]
    file_path = event["file_path"]

    print(f"Processing PDF: {file_id}")
    try:
        parsed = parse_pdf(file_path)

        result = {
            "file_id": file_id,
            "original_filename": event["original_filename"],
            "status": "processed",
            "parsed": parsed
        }

        output_path = save_result(file_id, result)

        print(f"Saved result: {output_path}")

    except Exception as error:
        print(f"Error processing {file_id}: {error}")