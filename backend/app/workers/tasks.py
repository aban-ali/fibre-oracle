from app.workers.celery_app import celery_app

@celery_app.task
def process_image(image_id: str):
    print(f"Processing image with ID: {image_id}")
    # CV logic comming soon
    print(f"Finished processing image with ID: {image_id}")