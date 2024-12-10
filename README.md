# Real-Time Road Width Measurement from Video
This project implements a real-time system to measure the width of a road from a video using computer vision and object detection techniques.The system leverages YOLOv8 for object detection and OpenCV for video processing, with the aim of estimating road dimensions accurately by analyzing detected vehicles in the video.

*Features*
Extracts video frames for individual analysis.
Detects objects (vehicles) in each frame using YOLOv8.
Calibrates pixel dimensions to real-world measurements using reference objects.
Estimates road width dynamically across video frames.
Tracks detected vehicles to improve consistency in width measurement.
Visualizes results by overlaying bounding boxes and road width on video.
Outputs results as a processed video and a summary text file.
*Technologies Used*
*Python:* Primary programming language.
*YOLOv8:* Object detection framework.
*OpenCV:* Video processing and frame analysis.
*NumPy:* Numerical computations for calibration and measurement.
