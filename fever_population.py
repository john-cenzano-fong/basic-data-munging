import __future__
import csv
from datetime import datetime
import json

FEVER = 99.5

user_file_path = "user_data.csv"
reading_file_path = "readings.json"

with open(user_file_path, "r") as users_file:
    user_reader = csv.reader(users_file, delimiter=',')
    user_header = next(user_reader)

    # We want to turn this into a list of dicts
    user_data = [dict(zip(user_header, row)) for row in user_reader]

user_count = len(user_data)
print("User file ({}) records: {}".format(user_file_path, user_count))
with open(reading_file_path, "r") as readings:

    # Also make this a list of dicts
    reading_data = [json.loads(l) for l in readings.read().splitlines()]

reading_count = len(reading_data)
print("Reading file ({}) records: {}".format(reading_file_path, reading_count))

# Combine data
user_reading = []
for r in reading_data:
    for u in user_data:
        if u["user_id"] == r["user"]["id"]:

            """
            So you can do this with an update or cherry pick
            the fields and create a new dict. Cherry picking
            creates a cleaner output but may result in missed
            data in the future if files change. I prefer update
            so I don't have to actively maintain this section
            of code.
            """
            r.update(u)

            """
            Since we're producing our combined data set let's
            add a fever indicator
            """
            r["has_fever"] = r["temperature"] > FEVER
            user_reading.append(r)
            # Stop processing to save resources
            continue

# Quick reality checks
user_reading_count = len(user_reading)
if user_reading_count != reading_count:
    print("WARNING: input and joined counts don't match:" \
          "user_reading({ur}) vs. reading({r})".format(ur=user_reading_count,
                                                       r=reading_count))
else:
    print("Joined count matches reading data")

reading_with_fever = [i for i in user_reading if i["has_fever"]]
print("Fever entry count: {}".format(len(reading_with_fever)))

print("Fever Detection Results\n")
print("|Date\t\t|Zip\t|Unique Count\t|Total Count\t|Duplicate Detected\t|")
print("="*81)

"""
Though we know there is only one date right now, organize around dates
so we could produce results with date context and be confident all values
apply to the date
"""
fever = {}
for date_val in sorted(set([d["date"] for d in reading_with_fever])):
    fever[date_val] = {}
    for zip_code in sorted(set([d["zip"] for d in reading_with_fever if d["date"] == date_val])):
        fever[date_val][zip_code] = []
        for reading in reading_with_fever:
            if reading["date"] == date_val and reading["zip"] == zip_code:
                fever[date_val][zip_code].append(reading["user_id"])

        # Report results
        for reading in fever:
            unique_count = len(set(fever[date_val][zip_code]))
            total_count = len(fever[date_val][zip_code])
            extra_info = "\tX\t\t" if total_count > unique_count else "\t\t\t"
            print("|{date}\t|{zip}\t|{unique}\t\t|{total}\t\t|{extra}|".format(
                date=datetime.strptime(date_val, "%Y%m%d").date(),
                zip=zip_code, unique=unique_count, total=total_count,
                extra=extra_info))
