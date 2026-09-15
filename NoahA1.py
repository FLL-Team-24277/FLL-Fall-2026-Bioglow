from base_robot import *

# left side white
# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

    # dfd

    # tip
    br.moveRightAttachmentMotorForMillis(millis=200, speedPct=-120)
    br.moveLeftAttachmentMotorForMillis(millis=250, speedPct=160)
    br.driveForDistance(
        distance=-50, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveLeftAttachmentMotorForMillis(millis=380, speedPct=-80)

    br.driveForDistance(
        distance=-120, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForMillis(millis=250, speedPct=70)
    br.moveRightAttachmentMotorForMillis(millis=50, speedPct=40)
    br.driveForDistance(
        distance=-250, speedPct=80, then=Stop.BRAKE, waiting=True
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
