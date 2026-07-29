from base_robot import *

# Import missions
import m1_left, m1_right, m2_left, m2_right, m3_left, m3_right, m4_left, m4_right

br: BaseRobot = BaseRobot()

pressed = []
col: Color = br.colorSensor.color()


def get_selected_side() -> str:
    while True:
        current_color = br.colorSensor.color()

        # Show what color the robot currently sees.
        if current_color == Color.SENSOR_NONE:  # type: ignore
            br.hub.display.icon(Icon.SAD)
            br.hub.light.on(Color.RED)
        else:
            br.hub.display.icon(Icon.HAPPY)
            br.hub.light.on(br.myColor2DefaultColorDict[current_color])

        wait(50)
        current_buttons = br.hub.buttons.pressed()

        if Button.LEFT in current_buttons:
            return "left"

        if Button.RIGHT in current_buttons:
            return "right"

        if Button.BLUETOOTH in current_buttons:
            # Run the drive motors for wheel cleaning.
            br.driveForMillis(millis=30000, speedPct=100, gyro=False)


def launch_selected_mission(selected_color: Color, table_side: str):
    if selected_color == Color.SENSOR_BLUE:  # type: ignore
        if table_side == "left":
            print("Launching M1 left")
            m1_left.Run(br)
        else:
            print("Launching M1 right")
            m1_right.Run(br)
        return

    if selected_color == Color.SENSOR_RED:  # type: ignore
        if table_side == "left":
            print("Launching M2 left")
            m2_left.Run(br)
        else:
            print("Launching M2 right")
            m2_right.Run(br)
        return

    if selected_color == Color.SENSOR_YELLOW:  # type: ignore
        if table_side == "left":
            print("Launching M3 left")
            m3_left.Run(br)
        else:
            print("Launching M3 right")
            m3_right.Run(br)
        return
    if selected_color == Color.SENSOR_WHITE:  # type: ignore
        if table_side == "left":
            print("Launching M4 left")
            m4_left.Run(br)
        else:
            print("Launching M4 right")
            m4_right.Run(br)
        return

    print("No mission is assigned to that color.")
    br.hub.display.icon(Icon.SAD)
    br.hub.light.on(Color.RED)
    wait(1500)


while True:
    table_side = get_selected_side()
    col = br.colorSensor.color()
    launch_selected_mission(col, table_side)
