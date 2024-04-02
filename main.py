import pandas as pd
import datetime
dir = ["sample.csv", "sample2.csv"]
timestamp = pd.read_csv(dir[0]).InteractionId.apply(lambda x: datetime.datetime.utcfromtimestamp(x))
for path in dir:
    df = pd.read_csv(path)
    df["LoadTimeStamp"] = timestamp
    df.to_csv(path.split(".")[0] + " added_timestamp.csv", index= False)
