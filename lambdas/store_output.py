def lambda_handler(event, context):
    print("Storing result:", event)

    # Simulate storing output
    event["stored"] = True

    return {
        "message": "Stored successfully",
        "final_output": event
    }