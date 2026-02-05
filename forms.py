# forms.py
from django import forms

class PredictionForm(forms.Form):

    name_A = forms.CharField(label = 'Enter name of A: ', required= True)
    national_idA = forms.CharField(label = 'Enter A antional ID: ', required= True)
    vehicle_typeA = forms.CharField(label = 'Enter A vehicle Type: ', required= True)
    plate_A = forms.CharField(label = 'Enter A plate Number: ', required= True)
    license_A = forms.CharField(label = 'Enter A License Number: ', required= True)

    name_B = forms.CharField(label = 'Enter name of B: ', required= True)
    national_idB = forms.CharField(label = 'Enter B antional ID: ', required= True)
    vehicle_typeB = forms.CharField(label = 'Enter B vehicle Type: ', required= True)
    plate_B = forms.CharField(label = 'Enter B plate Number: ', required= True)
    license_B = forms.CharField(label = 'Enter A License Number: ', required= True)


    YES_NO_CHOICES = (
        (1, 'Yes'),  
        (0, 'No')    
    )

    image_a = forms.ImageField(label='Upload A image')
    image_b = forms.ImageField(label='Upload B image')
    
    feature_1 = forms.FloatField(label='Enter the number of cars involved in the accident')

    feature_2 = forms.ChoiceField(
        choices= ((21, 'Rear-end Collision'),(22, 'Side-Swipe')),
        label='Collision Configuration',
        widget=forms.Select  
    )

    feature_3 = forms.ChoiceField(
        choices= ((2, 'Intersection'), (3, 'at intersection of at least two public roads'), (4, 'intersection with parking lot entrance/exit'),(5, 'RailRoad level Crossing')),
        label='Roadway Configuration',
        widget=forms.Select  # This makes it use radio buttons
    )

    feature_4 = forms.ChoiceField(
        choices= ((1, 'Straight'),(2, 'Straight with gradient'),(3, 'Curved'), (4, 'Curved with gradient')),
        label='Road Alignment',
        widget=forms.Select  # This makes it use radio buttons
    )

    feature_5 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        label='A was in Reverse?',
        widget=forms.Select  # This makes it use radio buttons
    )

    feature_6 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        label='B Was in Reverse?',
        widget=forms.Select  # This makes it use radio buttons
    )

    feature_7 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        label='A > speedLimit',
        widget=forms.Select  # This makes it use radio buttons
    )

    feature_8 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        label='B > speed Limit',
        widget=forms.Select  # This makes it use radio buttons
    )

    feature_9 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        label='A was parked?',
        widget=forms.Select  # This makes it use radio buttons
    )

    feature_10 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        label='B was parked?',
        widget=forms.Select  # This makes it use radio buttons
    )

    feature_11 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        label='A in Emergency Lane',
        widget=forms.Select  # This makes it use radio buttons
    )

    feature_12 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        label='B in Emergency Lane',
        widget=forms.Select  # This makes it use radio buttons
    )

    feature_13 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        label='A lights were On?',
        widget=forms.Select  # This makes it use radio buttons
    )


    feature_14 = forms.ChoiceField(
        choices = YES_NO_CHOICES,
        label='B lights were On?',
        widget=forms.Select  # This makes it use radio buttons
    )
    

