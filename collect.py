import requests
from data_types import MinerInput, MinerOutput
import json
import time

result = []
start_time = time.time()

def get_task(qid = -1):
  response = requests.get("http://localhost:10001/task", params={"qid": qid})
  response.raise_for_status()
  return response.json()

data = []

for qid in range(0, 500):
  for i in range(20):
    try:
      print(qid, i, time.time() - start_time)
      payload = get_task(qid)
      payload["qid"] = qid

      data.append(payload)
      if len(data) % 5 == 4:
        with open(f"0-500.json", "w") as f:
          json.dump(data, f, indent=2)

    except:
      print("Skip")

