from rest_framework.generics import ListAPIView
from main.models.vehicles import Vehicles
from .serializers import LogsSerializer
import pusher


class GetVehicleDetailsByDay(ListAPIView):
    serializer_class = LogsSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        year = int(self.request.GET["year"])
        month = int(self.request.GET["month"])
        day = int(self.request.GET["day"])

        vehicle = Vehicles.objects.get(pk=pk)
        selected_logs = vehicle.data_logs.filter(
            dt_log__year=year, dt_log__month=month, dt_log__day=day
        )

        return selected_logs
