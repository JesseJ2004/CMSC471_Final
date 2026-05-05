import json
def proxy_handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))

    return {}