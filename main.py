import time
import psutil

#  venv have psutil package 

def get_size(bytes):
    """Convert bytes to a human-readable format"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024

def monitor_bandwidth(interval=1):
    print("Monitoring network bandwidth... Press Ctrl+C to stop\n")
    
    old_data = psutil.net_io_counters()
    
    while True:
        time.sleep(interval)
        new_data = psutil.net_io_counters()
        
        # Calculate bytes sent/received per second
        bytes_sent = new_data.bytes_sent - old_data.bytes_sent
        bytes_recv = new_data.bytes_recv - old_data.bytes_recv
        
        upload_speed = get_size(bytes_sent / interval)
        download_speed = get_size(bytes_recv / interval)
        
        print(f"Upload Speed: {upload_speed}/s | Download Speed: {download_speed}/s")
        
        old_data = new_data

if __name__ == "__main__":
    try:                               
        monitor_bandwidth(interval=1)
    except KeyboardInterrupt:        # When we press ctrl + c ,it will raise a keyboard interrupt exception and while will stop.   
        print("\nMonitoring stopped.")   