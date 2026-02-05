# model.py
import torch
from torchvision import transforms
from PIL import Image
import torch
import numpy as np
from torch.utils.data import DataLoader, TensorDataset
import os
from .services.model import MultiInputModel

# Example instantiation with hypothetical values
num_numerical_features = 14 
num_output_classes = 5      

model = MultiInputModel(num_numerical_features=num_numerical_features, num_output_classes=num_output_classes)

# Build the path to the model file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'EstimateMeApp', 'resources', 'model.pth')

state_dict = torch.load(model_path,  map_location=torch.device('cpu'))
model.load_state_dict(state_dict)

model.eval()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def predict(image_a_file, image_b_file, features):
    
    transform = transforms.Compose([
    transforms.Resize((256, 384)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    image_a = Image.open(image_a_file)
    image_b = Image.open(image_b_file)

# Apply transformations
    image_a_tensor = transform(image_a).unsqueeze(0)  # Add batch dimension
    image_b_tensor = transform(image_b).unsqueeze(0)  # Add batch dimension

    # Prepare numerical data (example)
    numerical_data = features
    numerical_data_tensor = torch.tensor(numerical_data, dtype=torch.float).unsqueeze(0)  # Convert to tensor and add batch dimension



    # Assuming you have tensors new_images_a, new_images_b, and new_numerical_data
    new_dataset = TensorDataset(image_a_tensor, image_a_tensor, numerical_data_tensor)
    new_loader = DataLoader(new_dataset, batch_size=10, shuffle=False)

    model.eval()
    predictions = []
    with torch.no_grad():
        for (images_a, images_b, numerical_data) in new_loader:
            images_a = images_a.to(device)
            images_b = images_b.to(device)
            numerical_data = numerical_data.to(device)
            outputs = model(images_a, images_b, numerical_data)
            _, predicted = torch.max(outputs.data, 1)
            predictions.extend(predicted.cpu().numpy())
            result = predicted.cpu().numpy()
    return result
