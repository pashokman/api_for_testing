HOUSE = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "address": {"type": "string"},
            "id": {"type": "string", "format": "uuid"},
            "owner_ids": {"type": "array", "items": {"type": "string", "format": "uuid"}},
        },
        "required": ["title", "address", "id", "owner_ids"],
    },
}
