import cv2
import mediapipe as mp
import pyautogui
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

screen_width, screen_height = pyautogui.size()

cap = cv2.VideoCapture(1)

hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Flag to track dragging
dragging = False

def distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    gesture_text = ""

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            hand_type = handedness.classification[0].label
            landmarks = hand_landmarks.landmark

            # Get important landmarks
            x_index = int(landmarks[8].x * image.shape[1])
            y_index = int(landmarks[8].y * image.shape[0])

            x_thumb = int(landmarks[4].x * image.shape[1])
            y_thumb = int(landmarks[4].y * image.shape[0])

            x_middle = int(landmarks[12].x * image.shape[1])
            y_middle = int(landmarks[12].y * image.shape[0])

            dist_index_thumb = distance((x_index, y_index), (x_thumb, y_thumb))
            dist_middle_thumb = distance((x_middle, y_middle), (x_thumb, y_thumb))

            if hand_type == "Right":
                # Cursor move
                screen_x = int(landmarks[8].x * screen_width)
                screen_y = int(landmarks[8].y * screen_height)
                pyautogui.moveTo(screen_x, screen_y)
                gesture_text = "Moving Cursor"

            elif hand_type == "Left":
                if dist_index_thumb < 30:
                    if not dragging:
                        pyautogui.mouseDown()
                        dragging = True
                        gesture_text = "Start Drag"
                    else:
                        gesture_text = "Dragging..."

                elif dist_index_thumb > 60 and dragging:
                    pyautogui.mouseUp()
                    dragging = False
                    gesture_text = "Stop Drag"

                elif dist_middle_thumb < 40:
                    pyautogui.leftClick()
                    gesture_text = "Left Click"

                elif dist_index_thumb < 40:
                    pyautogui.rightClick()
                    gesture_text = "Right Click"

    if gesture_text:
        cv2.putText(image, gesture_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Gesture Control", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
