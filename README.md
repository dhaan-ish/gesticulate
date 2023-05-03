# gesticulate
# Hand Gesture Recognition

This project utilizes the Mediapipe library and OpenCV to perform hand gesture recognition from a video feed. It detects various hand landmarks and checks for specific hand configurations to recognize gestures.

## Prerequisites

Before running the code, make sure you have the following libraries installed:

- OpenCV: You can install it using `pip install opencv-python`.
- Mediapipe: You can install it using `pip install mediapipe`.
- Playsound: You can install it using `pip install playsound`.

## Getting Started

1. Clone the repository or download the code files.

2. Install the required dependencies as mentioned in the Prerequisites section.

3. Run the `hand_gesture_recognition.py` script.

4. The script will capture video from the default camera (you can replace it with your own video source if desired).

5. It will detect hand landmarks using Mediapipe and perform gesture recognition based on specific hand configurations.

6. Depending on the recognized gesture, the corresponding audio file will be played.

7. Press 'q' to quit the application.

## Customization

- If you want to use a different video source, replace the argument in `cv2.VideoCapture()` with the appropriate source (e.g., a video file path).

- To add or modify gestures, you can create additional functions for playing audio files and extend the conditional statements in the main loop (`while True`).

## Contributing

Contributions are welcome! If you find any issues or want to enhance the code, feel free to open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
