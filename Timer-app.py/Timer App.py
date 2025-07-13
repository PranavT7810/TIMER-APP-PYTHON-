import time
import playsound

def countdown_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds >= 0:
        hrs, remainder = divmod(total_seconds, 3600)
        mins, secs = divmod(remainder, 60)
        time_format = f"{hrs:02d}:{mins:02d}:{secs:02d}"
        print(f"\nTime left: {time_format}")
        time.sleep(1)
        total_seconds -= 1

    print("\nTime's up!")
    print("\nTHE ALARM PLAYS FOR 20 SECONDS!!")
    playsound.playsound('alarm_sound.mp3')
    print("\nAlarm Stopped")
    print("")
    print("")
if __name__ == "__main__":

    while True:
        try:
            print("### Timer App ###")
            print("\n### CODE BY T.HARIN PRANAV ###")
            print("")
            hrs = int(input("Enter Hours   : "))
            mins = int(input("Enter Minutes : "))
            secs = int(input("Enter Seconds : "))
            countdown_timer(hrs, mins, secs)
        except ValueError:
            print("\nPlease enter valid Time for hours, minutes, and seconds.")
            print("")
            print("")
