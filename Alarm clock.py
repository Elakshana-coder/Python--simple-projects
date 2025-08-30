import datetime
import time
import winsound

alarm_time = input("Enter the alarm time :")
print(f"⏰Alarm set for{alarm_time}...")

while True:
    now=datetime.datetime.now().strftime("%H:%M")
    if now == alarm_time:
        print("🔔Wake up!Time's Up!")

        for i in range(5):
            winsound.Beep(1000,1000)
        break

    time.sleep(30)
                   
