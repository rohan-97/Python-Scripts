import datetime

now = datetime.datetime.now()

print(str(now).replace("-","")[:8])