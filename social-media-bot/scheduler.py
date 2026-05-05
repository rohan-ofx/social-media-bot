import schedule
import time
from bot import auto_post
schedule.every(1).minutes.do(auto_post)

print("Scheduler started")
while True:
 schedule.run_pending()
 time.sleep(1)