from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import pandas as pd
from django.conf import settings
import os
from .services.model import load_model
from .forms import PredictionForm
from .model import predict
from .models import Accident
import uuid
#########################################






def view_accident_details(request, accident_id):
    # Retrieve the accident record by accident_id
    accident = get_object_or_404(Accident, accident_id=accident_id)
    return render(request, 'view_accident_details.html', {'accident': accident})

def prediction_view(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST, request.FILES)
        if form.is_valid():
            # Generate a unique Accident ID:
            accident_id = str(uuid.uuid4())
            # Process form data
            image_a_file = request.FILES['image_a']
            image_b_file = request.FILES['image_b']
            features = [float(form.cleaned_data['feature_1']), float(form.cleaned_data['feature_2']),
                         float(form.cleaned_data['feature_3']),
                         float(form.cleaned_data['feature_4']),
                         float(form.cleaned_data['feature_5']),
                         float(form.cleaned_data['feature_6']),
                         float(form.cleaned_data['feature_7']),
                         float(form.cleaned_data['feature_8']),
                         float(form.cleaned_data['feature_9']),
                         float(form.cleaned_data['feature_10']),
                         float(form.cleaned_data['feature_11']),
                         float(form.cleaned_data['feature_12']),
                         float(form.cleaned_data['feature_13']),
                         float(form.cleaned_data['feature_14']),
                        ]
            
            # Prediction
            result = predict(image_a_file, image_b_file, features)
            
            if result == 0:
                tempA = "100%"
                tempB = "0%"
            elif result == 1:
                tempA = "75%"
                tempB = "25%"
            elif result == 2:
                tempA = "50%"
                tempB = "50%"
            elif result == 3:
                tempA = "25%"
                tempB = "75%"
            elif result == 4:
                tempA = "0%"
                tempB = "100%"
            else:
                 tempA = "0"
                 tempB = "0"
               
            
            # Here you need to convert images and features into model input format
            # Create an Accident instance and save
            new_accident = Accident(
                accident_id=accident_id,
                name_A = form.cleaned_data['name_A'],
                national_idA = form.cleaned_data['national_idA'],
                vehicle_typeA = form.cleaned_data['vehicle_typeA'],
                plate_A = form.cleaned_data['plate_A'],
                license_A = form.cleaned_data['license_A'],

                name_B = form.cleaned_data['name_B'],
                national_idB = form.cleaned_data['national_idB'],
                vehicle_typeB = form.cleaned_data['vehicle_typeB'],
                plate_B = form.cleaned_data['plate_B'],
                license_B = form.cleaned_data['license_B'],

                image_a = form.cleaned_data['image_a'],
                image_b = form.cleaned_data['image_b'],
                feature_1 = form.cleaned_data['feature_1'],
                feature_2 = form.cleaned_data['feature_2'],
                feature_3 = form.cleaned_data['feature_3'],
                feature_4 = form.cleaned_data['feature_4'],
                feature_5 = form.cleaned_data['feature_5'],
                feature_6 = form.cleaned_data['feature_6'],
                feature_7 = form.cleaned_data['feature_7'],
                feature_8 = form.cleaned_data['feature_8'],
                feature_9 = form.cleaned_data['feature_9'],
                feature_10 = form.cleaned_data['feature_10'],
                feature_11 = form.cleaned_data['feature_11'],
                feature_12 = form.cleaned_data['feature_12'],
                feature_13 = form.cleaned_data['feature_13'],
                feature_14 = form.cleaned_data['feature_14'],
                liableA = tempA,
                liableB = tempB
                
                #objected = False,
            )
            new_accident.save()
            

            
            
            

            return render(request, 'result.html', {
                'accident_id': accident_id,
                'liableA': tempA,
                'liableB': tempB,
                'result': result
            })
    else:
        form = PredictionForm()
    return render(request, 'predict.html', {'form': form})

def home(request):
    return render(request, 'index.html')



def handle_previous_accident(request):
    if request.method == 'GET':
        accident_id = request.GET.get('accidentID')
        # Fetch details based on accident ID
        return redirect('view_accident_details', accident_id=accident_id)
    else:
        return redirect('home')
    
def submit_accident(request):
    if request.method == 'POST':
        # Process the form data
        secondPartyNumber = request.POST.get('secondPartyNumber')
        phoneNumber = request.POST.get('phoneNumber')
        
        # Here you might want to save data to the database or perform other actions
        
        # After processing, redirect to the new accident page
        return render(request, 'newAccident.html')
    else:
        # If not a POST request, just display the form again or redirect elsewhere
        return render(request, 'index.html')



def draw_accident(request):    
    return render(request,'newAccident.html')


def submit_response(request, accident_id):
    if request.method == 'POST':
        accident = Accident.objects.get(accident_id=accident_id)
        response = request.POST.get('response')
        if response == 'Accept':
            accident.status = 'Accepted'
        else:
            accident.status = 'Objected'
        accident.save()
        return redirect('home')  # Redirect to a confirmation page or back to the list
    return redirect('home')  # Handle error or invalid method
