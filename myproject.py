import tkinter as tk
import random


# 1. VARIABLES & DATA TYPES
# =====================================================
game_title: str = "F-15C Flight Sim UI"  # String data type
max_altitude: int = 15000              # Integer data type
fuel_level: float = 100.0              # Float data type
is_engine_on: bool = True              # Boolean data type
score: int = 0                         # Integer data type

# State dictionary (Data type: dict)
game_state = {
    "speed": 0,
    "throttle": 0,
    "gear_down": True,
    "survivors_saved": 0
}

# =====================================================
# 2. WORLD SETUP USING A WHILE LOOP
# =====================================================
# Procedurally generating cloud locations using a while loop
cloud_list = []
clouds_generated = 0
while clouds_generated < 5:  # <--- WHILE LOOP REQUIREMENT
    cloud_x = random.randint(-100, 100)
    cloud_z = random.randint(100, 500)
    cloud_list.append((cloud_x, cloud_z))
    clouds_generated += 1

# =====================================================
# 3. TKINTER GUI WINDOW SETUP
# =====================================================
root = tk.Tk()
root.title(game_title)
root.geometry("400x350")
root.config(bg="#112233")

# Title Label
title_label = tk.Label(root, text="--- F-15C KADENA ZZ-097 ---", font=("Courier", 14, "bold"), bg="#112233", fg="#00ff66")
title_label.pack(pady=10)

# Status Display Label
status_text = f"Throttle: {game_state['throttle']}%\nSpeed: {game_state['speed']} KTS\nGear: DOWN\nSaved: {game_state['survivors_saved']}/5"
status_label = tk.Label(root, text=status_text, font=("Courier", 11), bg="#112233", fg="#00ff66", justify=tk.LEFT)
status_label.pack(pady=10)

# Message/Banner Label
message_label = tk.Label(root, text="Ready for takeoff!", font=("Courier", 10, "italic"), bg="#112233", fg="#ffeb3b")
message_label.pack(pady=5)

# =====================================================
# 4. GAME FUNCTIONS (WITH IF STATEMENTS)
# =====================================================
def increase_throttle():
    # IF STATEMENTS REQUIREMENT
    if game_state["throttle"] < 100:
        game_state["throttle"] += 25
        game_state["speed"] = game_state["throttle"] * 2
        message_label.config(text="Afterburners engaged!")
    else:
        message_label.config(text="Throttle is already at maximum!")
    update_ui()

def toggle_gear():
    # IF STATEMENTS REQUIREMENT
    if game_state["gear_down"]:
        game_state["gear_down"] = False
        message_label.config(text="Landing gear retracted.")
    else:
        game_state["gear_down"] = True
        message_label.config(text="Landing gear deployed.")
    update_ui()

def check_rescue():
    # IF STATEMENTS REQUIREMENT
    if not game_state["gear_down"] and game_state["speed"] > 100:
        game_state["survivors_saved"] += 1
        message_label.config(text="Survivor rescued successfully!")
        if game_state["survivors_saved"] >= 5:
            message_label.config(text="MISSION COMPLETE! All survivors saved!")
    else:
        message_label.config(text="Fly faster and retract gear to rescue survivors!")
    update_ui()

def update_ui():
    gear_str = "DOWN" if game_state["gear_down"] else "RETRACTED"
    status_label.config(
        text=f"Throttle: {game_state['throttle']}%\n"
             f"Speed: {game_state['speed']} KTS\n"
             f"Gear: {gear_str}\n"
             f"Saved: {game_state['survivors_saved']}/5"
    )

# =====================================================
# 5. UI BUTTON CONTROLS
# =====================================================
throttle_btn = tk.Button(root, text="Increase Throttle [+25%]", font=("Courier", 10, "bold"), bg="#ff5500", fg="white", command=increase_throttle)
throttle_btn.pack(pady=5, fill=tk.X, padx=40)

gear_btn = tk.Button(root, text="Toggle Landing Gear [G]", font=("Courier", 10, "bold"), bg="#0088cc", fg="white", command=toggle_gear)
gear_btn.pack(pady=5, fill=tk.X, padx=40)

rescue_btn = tk.Button(root, text="Attempt SAR Rescue Pass", font=("Courier", 10, "bold"), bg="#00aa44", fg="white", command=check_rescue)
rescue_btn.pack(pady=5, fill=tk.X, padx=40)

# Start the Tkinter GUI loop
root.mainloop()