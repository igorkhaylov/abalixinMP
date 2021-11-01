from datetime import datetime, timedelta


date = datetime.now()

dates = []

for i in range(10):
    dates.append(date)
    date = date - timedelta(days=1)
