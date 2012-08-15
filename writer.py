import csv


def exportTimeline(file, timelineData):
        csvWriter = csv.writer(file)
        for post in timelineData:
            user = post["user"]
            name = user["first_name"]
            name = name + " " + user["last_name"]
            name = name.encode("UTF-8")
            time = post["created_at"]
            time = time.encode("UTF-8")
            text = post["text"].encode("UTF-8")
            csvWriter.writerow([name, time, text])
