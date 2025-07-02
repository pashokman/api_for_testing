CARS_WITHOUT_GARAGE = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "model": {"type": "string"},
            "garage_id": {"type": "null"},
            "id": {"type": "string", "format": "uuid"},
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
        "required": ["model", "garage_id", "id", "owners"],
    },
}

CAR_WITH_GARAGE = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "model": {"type": "string"},
            "garage_id": {"type": "string", "format": "uuid"},
            "id": {"type": "string", "format": "uuid"},
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
        "required": ["model", "garage_id", "id", "owners"],
    },
}
