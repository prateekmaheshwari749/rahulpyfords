import pandas as pd
import random

data = []

for i in range(500):

    screen = random.randint(1, 12)
    social = random.randint(0, screen)
    sleep = random.randint(3, 9)
    study = random.randint(0, 8)
    notifications = random.randint(10, 150)

    if screen <= 3 and sleep >= 7 and study >= 4:
        addiction = 0   # Normal
    elif screen <= 6:
        addiction = 1   # Risk
    else:
        addiction = 2   # Addicted

    data.append([screen, social, sleep, study, notifications, addiction])

df = pd.DataFrame(data, columns=[
    "ScreenTime",
    "SocialMediaTime",
    "SleepHours",
    "StudyHours",
    "Notifications",
    "AddictionLevel"
])

df.to_csv("mobile_addiction_dataset.csv", index=False)

print("Dataset Created!")