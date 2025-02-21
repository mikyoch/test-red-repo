import requests
from data_types import MinerInput, MinerOutput
import json
import time
from pathlib import Path

result = []
start_time = time.time()

def get_task(qid = -1):
  response = requests.get("http://localhost:10001/task", params={"qid": qid})
  response.raise_for_status()
  return response.json()

ID = 11
st = ID * 250
ed = st + 250

directory = Path(f"./{st}-{ed}")
directory.mkdir(parents=True, exist_ok=True)

for qid in range(st, ed):
  data = []
  for i in range(20):
    try:
      print(qid, i, time.time() - start_time)
      payload = get_task(qid)
      payload["qid"] = qid

      data.append(payload)
      if len(data) % 5 == 0:
        with open(f"./{st}-{ed}/{qid}.json", "w") as f:
          json.dump(data, f, indent=2)

    except:
      print("Skip")

