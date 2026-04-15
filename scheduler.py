from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from job import download_dataset
from config import JOB_INTERVAL_MINUTES, DEFAULT_PROJECT_ID

def start_scheduler():
    """
    Starts the APScheduler for periodic dataset downloads.
    """
    scheduler = BlockingScheduler()
    
    # Add job for periodic downloads
    scheduler.add_job(
        download_dataset,
        trigger=IntervalTrigger(minutes=JOB_INTERVAL_MINUTES),
        args=[DEFAULT_PROJECT_ID],
        id="dataset_download_job",
        name="Dataset Download Job",
        replace_existing=True
    )
    
    print(f"Starting APScheduler with interval: {JOB_INTERVAL_MINUTES} minutes")
    print(f"Monitoring project ID: {DEFAULT_PROJECT_ID}")
    
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
