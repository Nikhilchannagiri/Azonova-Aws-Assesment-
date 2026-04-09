def lambda_handler(event, context):
    print("Received event:", event)

    # Validate input
    if "job_id" not in event:
        raise Exception("Invalid input: job_id missing")

    return {
        "message": "Input validated",
        "data": event
    }