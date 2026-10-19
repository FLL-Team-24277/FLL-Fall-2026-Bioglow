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
    br.driveArcDist(
        radius=175, dist=150, speedPct=80, then=Stop.NONE, waiting=True
    )
    br.driveForDistance(
        distance=235, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveLeftAttachmentMotorForDegrees(degrees=90, speedPct=80)
    br.driveForDistance(
        distance=-140, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveLeftAttachmentMotorForDegrees(degrees=-90, speedPct=80)
    br.driveArcDist(
        radius=480, dist=400, speedPct=80, then=Stop.NONE, waiting=True
    )
    br.driveForDistance(
        distance=60, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForMillis(millis=360, speedPct=80)
    wait(1000)
    br.driveArcDist(
        radius=-780, dist=30, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveLeftAttachmentMotorForDegrees(degrees=85, speedPct=80)
    br.driveForDistance(
        distance=-70, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveLeftAttachmentMotorForDegrees(degrees=-15, speedPct=80)
    br.driveArcDist(
        radius=100, dist=50, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.driveForDistance(
        distance=300, speedPct=80, then=Stop.BRAKE, waiting=True
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
