from interface.models import Trajectory
import csv


def write_trajectories_to_file(file_path):
    all_trajectories = Trajectory.objects.all()
    data = []

    for tr in all_trajectories:
        row = tr.trajectory.split(",")
        data.append(row)

    with open(file_path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


