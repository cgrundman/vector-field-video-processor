# import cv2

# def process_video(video_path):
#     # Open the video file using OpenCV
#     cap = cv2.VideoCapture(video_path)

#     # Check if the video file is successfully opened
#     if not cap.isOpened():
#         print("Error: Could not open video.")
#         return

#     while True:
#         # Read each frame from the video
#         ret, frame = cap.read()

#         # If frame is read correctly, ret is True
#         if not ret:
#             print("End of video.")
#             break

#         # Process the frame (e.g., convert to grayscale)
#         gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # Display the frame
#         cv2.imshow("Processed Video", gray_frame)

#         # Break the loop if the 'q' key is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the video capture object and close windows
#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     video_path = "sample.mp4"
#     process_video(video_path)

import cv2

print(cv2.__version__)
