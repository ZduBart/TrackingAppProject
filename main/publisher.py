import pusher
import time
from threading import Thread
from .publisher_credentials import pusher_client


class PublisherThread(Thread):
    def run(self):
        from main.models.logs import DataLogs
        from vehicles_details_api.serializers import LogsSerializer

        first_logs = None
        # selected_logs = list(map(lambda vehicle: vehicle.data_logs.first(), vehicles))
        print(first_logs, flush=True)
        # serialized_logs = LogsSerializer(first_logs, many=True).data

        while True:
            logs = DataLogs.objects.last()
            serialized_logs = LogsSerializer(logs).data
            print(serialized_logs, flush=True)
            # if logs != first_logs:
            pusher_client.trigger("my-channel", "my-event", {"logs": serialized_logs})
            first_logs = logs

            time.sleep(2)
