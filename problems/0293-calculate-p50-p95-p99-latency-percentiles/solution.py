import numpy as np

def calculate_latency_percentiles(latencies: list[float]) -> dict[str, float]:
    if not latencies:
        return {"P50":0.0,"P95":0.0,"P99":0.0}
    else:
        return {
            "P50":round(float(np.percentile(latencies,50)),4),
            "P95":round(float(np.percentile(latencies,95)),4),
            "P99":round(float(np.percentile(latencies,99)),4)
        }