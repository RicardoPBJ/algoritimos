def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for p in permanence_period:
            if p[0] <= target_time <= p[1]:
                count += 1
        return count
    except Exception:
        return None