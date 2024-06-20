import tkinter as tk
from tkinter import ttk
import uuid
import cv2
import mediapipe as mp
import pyautogui
from PIL import Image, ImageTk

# Define the list of food items
foods = ["Burger", "Fries", "Pizza", "Salad", "Soda"]


# Function to handle ordering
# Function to handle ordering
def order_food():
    print("Ordering food...")
    selected_items = [food.get() for food in food_vars]
    selected_foods = [foods[index] for index, value in enumerate(selected_items) if value == 1]
    if selected_foods:
        order_id = str(uuid.uuid4())[:8]  # Generate a unique order ID
        print("Order ID:", order_id)
        print("Ordered items:")
        for food in selected_foods:
            print(" -", food)
        # Clear the selection of checkboxes
        for var in food_vars:
            var.set(0)
    else:
        print("Please select at least one item to order.")



# Create main window
root = tk.Tk()
root.title("Restaurant Food Ordering")
root.geometry("400x300")  # Set window size

# Frame to hold food items
food_frame = tk.Frame(root)
food_frame.pack(pady=10)

# Initialize food_vars list
food_vars = []

# Create checkboxes for each food item
food_icons = ["burger.png", "french-fries.png", "pizza.png", "salad.png", "soft-drink.png"]
for idx, food in enumerate(foods):
    var = tk.IntVar(value=0)
    food_vars.append(var)

    # Load food icon
    icon = Image.open(food_icons[idx])
    icon = icon.resize((30, 30), Image.ANTIALIAS)
    icon = ImageTk.PhotoImage(icon)

    # Create a themed checkbox with food icon
    chk = ttk.Checkbutton(food_frame, text=food, variable=var, onvalue=1, offvalue=0, image=icon, compound=tk.LEFT)
    chk.image = icon  # Keep a reference to prevent garbage collection
    chk.pack(anchor='w', padx=10, pady=5)

# Create Order Now button
order_button = tk.Button(root, text="Order Now", command=order_food, font=("Arial", 14), bg="green", fg="white")
order_button.pack(pady=10)

# Initialize computer vision
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

# Global variables for hand positions
index_x = 0
index_y = 0


# Function to detect hand gestures and control mouse cursor
def detect_gestures():
    global index_x, index_y
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:  # Tip of index finger
                    index_x = x
                    index_y = y
                    pyautogui.moveTo(index_x, index_y)
                if id == 4:  # Tip of thumb
                    thumb_x = x
                    thumb_y = y
                    if abs(index_y - thumb_y) < 50:
                        pyautogui.click()
                        pyautogui.sleep(1)
    root.after(100, detect_gestures)


# Start gesture detection loop
detect_gestures()

# Run the main event loop
root.mainloop()
