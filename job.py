import os
import requests
import json
from datetime import datetime
from config import API_BASE_URL, DOWNLOADS_DIR, METADATA_FILE

def download_dataset(project_id: str, format: str = "json"):
    """
    Downloads raw data from the specified project dataset endpoint.
    
    Args:
        project_id (str): The ID of the project.
        format (str): The format of the data (default is 'json').
    """
    url = f"{API_BASE_URL}/projects/{project_id}/dataset"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"dataset_{project_id}_{timestamp}.{format}"
    filepath = os.path.join(DOWNLOADS_DIR, filename)

    try:
        response = requests.get(url, params={"format": format}, timeout=30)
        response.raise_for_status()
        
        # Save the content
        with open(filepath, "wb") as f:
            f.write(response.content)
            
        # Register metadata
        log_metadata(project_id, format, len(response.content), filepath)
        print(f"Successfully downloaded dataset for project {project_id} to {filepath}")
        
    except Exception as e:
        print(f"Error downloading dataset for project {project_id}: {e}")
        # Optionally log failure in metadata
        log_metadata(project_id, format, 0, None, str(e))

def log_metadata(project_id: str, format: str, size: int, filepath: str | None, error: str | None = None):
    """
    Logs execution metadata for auditing.
    """
    metadata = {
        "timestamp": datetime.now().isoformat(),
        "project_id": project_id,
        "format": format,
        "size_bytes": size,
        "filepath": filepath,
        "error": error,
        "status": "success" if error is None else "failed"
    }
    
    # Append metadata to a JSONL file
    with open(METADATA_FILE, "a") as f:
        f.write(json.dumps(metadata) + "\n")
