# Gesture_Controlled_Food_ordering

This project is a Gesture Controlled Food Ordering System built using Python's Tkinter library for the GUI, PIL for image handling, and OpenCV and MediaPipe for gesture detection. The application allows users to browse through menu items, add them to the cart, and checkout. The application also supports hand gesture detection to navigate and select items.

## Features

- **Menu Browsing**: Users can browse through different categories of menu items.
- **Cart Management**: Users can add items to the cart, update quantities, and view the total price.
- **Checkout**: Users can confirm their order and see a detailed bill.
- **Hand Gesture Detection**: Users can interact with the application using hand gestures.

## Requirements

- Python 3.x
- Tkinter
- PIL (Pillow)
- OpenCV
- MediaPipe
- PyAutoGUI
- ttkbootstrap

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gesture-controlled-food-ordering-system.git
   cd gesture-controlled-food-ordering-system` 

2. Install the required packages:
   
    
    `pip install -r requirements.txt` 
    
3. Ensure you have a working webcam as it is required for hand gesture detection.
    

## Usage

Run the application:

`python main.py` 

## File Structure

- `main.py`: The main script that runs the application.
- `images/`: Directory containing images of menu items.
