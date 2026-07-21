# Application Requirements

Create a small service in **Go** or **Python** with the following endpoints.

## Required Endpoints

### `GET /health`

**Response:**

```json
{
    "status": "ok"
}
```

### `GET /version`

**Response:**

```json
{
    "version": "1.0.0"
}
```

### `GET /env`

**Response:**

```json
{
    "environment": "<value from ENVIRONMENT variable>"
}
```

### `POST /config`

**Request:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

**Response:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

### `GET /config/{name}`

**Example:**

```bash
GET /config/database_url
```

**Response:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

### `DELETE /config/{name}`

**Response:**

```json
{
    "deleted": true
}
```

## Implementation Notes

Use any framework you prefer.

## Testing cheatsheet

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/version
curl http://127.0.0.1:8000/env

curl -X POST http://127.0.0.1:8000/config \
  -H "Content-Type: application/json" \
  -d '{"name":"database_url","value":"postgres://example"}'

curl http://127.0.0.1:8000/config/database_url
curl -X DELETE http://127.0.0.1:8000/config/database_url
```