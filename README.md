# YOLOv8 Object Detection Model

This repository contains a trained YOLOv8 model (`best_new.pt`) and a Python script (`run_predictions.py`) for running object detection on new images. This model can detect specified objects in images and outputs the results with annotations.

## Contents
- `best_new.pt`: Trained YOLOv8 model weights file
- `run_predictions.py`: Python script for loading the model and running predictions on a specified image
- `README.md`: Instructions for setting up and using this repository

## Setup Instructions

### 1. Clone the Repository
Begin by cloning the repository to your local machine:

```bash
git clone https://github.com/Abhinavvvkk07/new_repo_object.git
cd new_repo_object

 ### 2. Install Required Dependencies
This model uses YOLOv8, which requires the ultralytics package. Ensure you have Python installed, then install the necessary dependencies:

bash
Copy code
pip install ultralytics
This will install YOLOv8 and other essential libraries for running predictions.

### 3. Verify the Model File
Ensure best_new.pt is present in the repository. This is the YOLOv8 model file needed to run predictions. It should be located in the root directory of this repository.

Running Predictions
The run_predictions.py script allows you to test the model on an image.

Instructions to Test the Model
Prepare an Image: Place your test image in a known location on your system or use an existing image path.

Run the Script: Use the following command, replacing "/path/to/your/image.jpg" with the path to your test image:

bash
Copy code
python run_predictions.py "/path/to/your/image.jpg"
Example:

bash
Copy code
python run_predictions.py "/Users/abhinavkumar/Downloads/Images 2"
Viewing Results
After running the prediction, the output image(s) will be saved in a new directory: runs/detect/predict. This folder will contain the annotated image(s) with bounding boxes around detected objects.

### 4. To view the results:

On macOS, open the folder with:

bash
Copy code
open runs/detect/predict
On Linux, use:

bash
Copy code
xdg-open runs/detect/predict
