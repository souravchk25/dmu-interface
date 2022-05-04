from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from interface.models import Trajectory
from interface.forms import TrajectoryForm
import mimetypes
import os
from interface.helper import write_trajectories_to_file


def index(request):
    if request.method == 'POST':
        need = request.POST['need']
        if need == 'Add Trajectory':
            return HttpResponseRedirect('addTrajectory/')
        elif need == 'View All':
            return HttpResponseRedirect('viewTrajectories/')
        elif need == 'Download Trajectories':
            return HttpResponseRedirect('download/')
    return render(request, 'interface/index.html')


def add_trajectory(request):
    if request.method == 'POST':
        form = TrajectoryForm(request.POST)

        if form.is_valid():
            # add trajectory to DB
            Trajectory.objects.create(trajectory=form.clean_trajectory())
            context = {
                "form": form,
                "message": "Successfully added the trajectory - {}".format(form.clean_trajectory())
            }
            return render(request, 'interface/add_trajectory.html', context)

    else:
        form = TrajectoryForm()
        context = {
            "form": form,
            "message": ""
        }
        return render(request, 'interface/add_trajectory.html', context)


def get_all_trajectories(request):
    if request.method == 'GET':
        all_trajectories = Trajectory.objects.all()
        trajectories = []
        for tr in all_trajectories:
            trajectories.append(tr.trajectory)
        context = {
            'trajectories': trajectories,
            'total': len(trajectories)
        }
        return render(request, 'interface/view_trajectories.html', context)

    else:
        return HttpResponse(status=405)


def download_trajectories(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = base_dir + "trajectories.csv"

    write_trajectories_to_file(file_path)
    path = open(file_path, 'r')
    mime_type, _ = mimetypes.guess_type(file_path)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filepath={}".format(file_path)
    return response

