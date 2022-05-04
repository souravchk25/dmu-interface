from django import forms


class TrajectoryForm(forms.Form):
    trajectory = forms.CharField(
        label="Enter",
        required=True
    )

    def clean_trajectory(self):
        clean_trajectory = self.cleaned_data['trajectory']

        # for now just return
        return clean_trajectory
