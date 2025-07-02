GARAGES_WITHOUT_HOUSE = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "id": {"type": "string", "format": "uuid"},
            "house_id": {"type": "null"},
            "owners": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"},
                        "email": {"type": "string", "format": "email"},
                        "id": {"type": "string", "format": "uuid"},
                        "is_admin": {"type": "boolean"},
                    },
                    "required": ["username", "email", "id", "is_admin"],
                },
            },
        },
        "required": ["title", "id", "house_id", "owners"],
    },
}

GARAGES_WITH_HOUSE = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "id": {"type": "string", "format": "uuid"},
            "house_id": {"type": "string", "format": "uuid"},
            "owners": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"},
                        "email": {"type": "string", "format": "email"},
                        "id": {"type": "string", "format": "uuid"},
                        "is_admin": {"type": "boolean"},
                    },
                    "required": ["username", "email", "id", "is_admin"],
                },
            },
        },
        "required": ["title", "id", "house_id", "owners"],
    },
}
