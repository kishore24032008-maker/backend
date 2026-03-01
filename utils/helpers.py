def calculate_percentage(part: float, total: float) -> float:
    if total == 0:
        return 0
    return round((part / total) * 100, 1)