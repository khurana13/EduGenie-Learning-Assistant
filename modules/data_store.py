import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("data/history.json")


def save_activity(task_type, user_input, output):
    DATA_FILE.parent.mkdir(exist_ok=True)

    if DATA_FILE.exists():
        try:
            records = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except Exception:
            records = []
    else:
        records = []

    records.append(
        {
            "id": len(records) + 1,
            "task_type": task_type,
            "user_input": user_input,
            "output": output,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    )

    DATA_FILE.write_text(json.dumps(records, indent=2), encoding="utf-8")
