from ultralytics import YOLO
import sys

# Load the model
model = YOLO('best_new.pt')  # Ensure this file is in the same directory

# Run predictions on an image file passed as a command-line argument
if len(sys.argv) > 1:
    image_path = sys.argv[1]  # Get the image path from the command linee
    results = model.predict(source=image_path, save=True)
    print(f"Results saved in: {results[0].save_dir}")
else:
    print("Please provide the path to an image. Usage: python run_predictions.py /path/to/image.jpg")
