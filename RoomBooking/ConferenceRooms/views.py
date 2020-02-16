from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from ConferenceRooms.models import Room, Reservation


# Create your views here.

class RoomNew(View):
    def get(self, request):
        return render(request, "Rooms.html", {})

    def post(self, request):
        name = request.POST.get("name")
        capacity = request.POST.get("capacity")
        projector = request.POST.get("projector")
        projector = bool(projector)
        Room.objects.create(name=name, capacity=capacity, projector=projector)
        return HttpResponseRedirect('/reservation/')


class RoomModify(View):
    pass


class RoomDelete(View):
    pass


def room_list(request):
    r = Room.objects.all()
    return HttpResponse(r)


class Reserve(View):
    def get(self, request):
        return render(request, "Reservation.html", {})

    def post(self, request):
        date = request.POST.get("date")
        room_id = request.POST.get("room_id")
        comments = request.POST.get("comments")
        Reservation.objects.create(date=date, room_id=room_id, comments=comments)
        if room_id and date is not None:
            return HttpResponse("Room is already booked")
        else:
            return HttpResponse("Reservation created")
