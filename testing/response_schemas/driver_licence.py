DRIVER_LICENCE = {
    "type": "object",
    "properties": {
        "licence_number": {"type": "string"},
        "user_id": {"type": "string", "format": "uuid"},
        "id": {"type": "string", "format": "uuid"},
    },
    "required": ["licence_number", "user_id", "id"],
}
