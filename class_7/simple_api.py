from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
import psutil
import uvicorn
from datetime import datetime

class SystemStats(BaseModel):
    """Model for system statistics."""
    cpu_percent: float
    memory_percent: float
    disk_percent: float
    boot_time: str

class ProcessInfo(BaseModel):
    """Model for process information."""
    pid: int
    name: str
    cpu_percent: float
    memory_percent: float

class SystemAPI:
    """Simple system monitoring API."""
    
    def __init__(self):
        self.app = FastAPI(
            title="Simple System Monitor",
            description="A simple API for monitoring system resources",
            version="1.0.0"
        )
        self.setup_routes()

    def get_system_stats(self) -> Dict:
        """Get basic system statistics."""
        return {
            "cpu_percent": psutil.cpu_percent(),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_percent": psutil.disk_usage('/').percent,
            "boot_time": datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')
        }

    def get_processes(self) -> List[Dict]:
        """Get list of running processes."""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return processes

    def setup_routes(self):
        """Setup API routes."""
        
        @self.app.get("/")
        async def root():
            """Root endpoint."""
            return {"message": "System Monitor API is running"}

        @self.app.get("/stats", response_model=SystemStats)
        async def get_stats():
            """Get system statistics."""
            try:
                return self.get_system_stats()
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.app.get("/processes", response_model=List[ProcessInfo])
        async def list_processes():
            """Get list of running processes."""
            try:
                return self.get_processes()
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

    def run(self, host: str = "127.0.0.1", port: int = 8000):
        """Run the FastAPI application."""
        uvicorn.run(self.app, host=host, port=port)

def main():
    api = SystemAPI()
    api.run()

if __name__ == "__main__":
    main() 