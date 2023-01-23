from random import randint


def generate_logs() -> list:
    log_list = []
    for i in range(17, 20):
        for j in range(8, 17):
            if len(str(j)) == 1:
                j = f"0{j}"

            log_list.append(
                {
                    "model": "main.datalogs",
                    # "pk": i+j+2,
                    "fields": {
                        "device_id": 1,
                        "vehicle_id": 1,
                        "dt_log": f"2022-05-{i}T{j}:00:00Z",
                        "latitude": f"50.087{randint(0,999)}",
                        "longitude": f"19.965{randint(0,999)}",
                        "engine_rpm": randint(1000, 1500),
                        "engine_on": True,
                        "coolant_temp": randint(50, 90),
                        "oil_temp": randint(70, 140),
                        "active_log": True,
                    },
                }
            )
    return log_list


print(generate_logs())
