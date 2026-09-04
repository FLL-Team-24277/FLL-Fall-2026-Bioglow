from base_robot import *

# right side white
# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

    # dfd

    br.driveForDistance(
        distance=245, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveLeftAttachmentMotorForDegrees(degrees=-30, speedPct=10)
    br.moveLeftAttachmentMotorForDegrees(degrees=40, speedPct=55)
    br.moveRightAttachmentMotorForMillis(millis=600, speedPct=-80)
    br.driveForDistance(
        distance=-125, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForMillis(millis=600, speedPct=+80)
    # br.moveRightAttachmentMotorForDegrees(degrees=50, speedPct=80)
    br.driveForDistance(
        distance=-130, speedPct=600, then=Stop.BRAKE, waiting=True
    )
    br.moveLeftAttachmentMotorForDegrees(degrees=-10, speedPct=80)
    # tip  cc


# Leave everything below here and don't type anything below this line
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
