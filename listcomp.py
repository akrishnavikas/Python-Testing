logs = [
    "2025-09-22 12:00:00 ERROR DataNode failed",
    "2025-09-22 12:01:00 INFO Job started",
    "2025-09-22 12:02:00 ERROR NameNode crashed",
    "2025-09-22 12:03:00 WARN Low disk space",
    "2025-09-20"
]


error_lines = [line for line in logs if "ERROR" in line]

print(error_lines)