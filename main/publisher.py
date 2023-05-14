import time
from threading import Thread

import pusher

from .publisher_credentials import pusher_client


class PublisherThread(Thread):
    def run(self):
        from main.models.logs import DataLogs
        from vehicles_details_api.serializers import LogsSerializer

        first_logs = None

        while True:
            logs = DataLogs.objects.last()
            serialized_logs = LogsSerializer(logs).data
            print(serialized_logs, flush=True)
            pusher_client.trigger("my-channel", "my-event", {"logs": serialized_logs})
            first_logs = logs

            time.sleep(2)
