# Simple System Monitor API

A minimal FastAPI application for monitoring system resources and listing running processes, built using Object-Oriented Programming (OOP) principles.

## Features
- Get basic system statistics (CPU, memory, disk usage, boot time)
- List all running processes with their resource usage
- Clean, simple codebase using OOP concepts
- Automatic interactive API docs via Swagger UI

## Requirements
- Python 3.8+
- See `requirements.txt` for dependencies

## Installation
1. Clone this repository or copy the files to your project directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the API server with:
```bash
python simple_api.py
```

The server will start at `http://127.0.0.1:8000/` by default.

## API Endpoints
- `GET /` — Root endpoint, returns a welcome message.
- `GET /stats` — Returns system statistics (CPU, memory, disk, boot time).
- `GET /processes` — Returns a list of running processes with their PID, name, CPU, and memory usage.

## API Documentation
Interactive documentation is available at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Example Usage
Get system stats:
```bash
curl http://127.0.0.1:8000/stats
```

List running processes:
```bash
curl http://127.0.0.1:8000/processes
```

## License
This project is provided for educational purposes. 