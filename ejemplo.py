import tkinter as tk

def on_button_press(event):
    # Store the initial coordinates of the mouse click and the item's ID
    event.widget.start_x = event.x
    event.widget.start_y = event.y
    # Use 'current' tag to refer to the item directly under the mouse
    event.widget.tag_bind(tk.CURRENT, "<B1-Motion>", on_mouse_motion)
    event.widget.tag_bind(tk.CURRENT, "<ButtonRelease-1>", on_button_release)

def on_mouse_motion(event):
    # Calculate the delta (difference) from the starting position
    dx = event.x - event.widget.start_x
    dy = event.y - event.widget.start_y
    # Move the 'current' item by the calculated delta
    event.widget.move(tk.CURRENT, dx, dy)
    # Update the starting position for the next motion event
    event.widget.start_x = event.x
    event.widget.start_y = event.y

def on_button_release(event):
    # Unbind the motion and release events when the button is released
    event.widget.tag_unbind(tk.CURRENT, "<B1-Motion>")
    event.widget.tag_unbind(tk.CURRENT, "<ButtonRelease-1>")

# --- Main application setup ---
root = tk.Tk()
root.title("Canvas Mouse Follow")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Create a rectangle and assign a tag for easy reference
# The 'draggable' tag allows us to bind events to this specific item
rect_item = canvas.create_rectangle(50, 50, 100, 100, fill="blue", tags="draggable")

# Bind the initial button press event to the canvas
# When the user clicks on the canvas, it will check if it's on an item
canvas.tag_bind("draggable", "<ButtonPress-1>", on_button_press)

root.mainloop()
