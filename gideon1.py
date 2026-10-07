from base_robot import *

# left side BLUE
# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call thi
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines
    br.driveForDistance(
        distance=660, speedPct=50, then=Stop.BRAKE, waiting=True
    )
    br.moveLeftAttachmentMotorForMillis(
        millis=1100, speedPct=100, waiting=True
    )
    br.turnInPlace(angle=-38, speedPct=15)
    br.driveForDistance(
        distance=150, speedPct=50, then=Stop.BRAKE, waiting=True
    )
    br.moveLeftAttachmentMotorForMillis(
        millis=1000, speedPct=-100, waiting=True
    )
    br.driveForDistance(
        distance=100, speedPct=50, then=Stop.BRAKE, waiting=True
    )
    br.curve(
        radius=-40, angle=-45, speedPct=100, then=Stop.BRAKE, waiting=True
    )
    br.driveForDistance(
        distance=-15, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    # Leave everything below here and don't type anything below this line


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
