USER = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "id": {"type": "string", "format": "uuid"},
        "is_admin": {"type": "boolean"},
    },
    "required": ["username", "email", "id", "is_admin"],
}
