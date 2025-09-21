import numpy as np

def rows_to_array(rows) -> tuple[np.ndarray, np.ndarray]:
    x = np.array([[row.steps_total, row.hr_avg, row.sleep_minutes] for row in rows])
    y = np.array([row.label for row in rows])
    return x, y
