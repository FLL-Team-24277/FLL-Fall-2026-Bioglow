from base_robot import *

# right side green
# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    # br.driveForDistance(
    #     distance=-400, speedPct=80, then=Stop.NONE, waiting=True
    # )
    br.driveArcDist(
        radius=500, dist=-500, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    # br.driveArcDist(
    #     radius=200, dist=-500, speedPct=80, then=Stop.BRAKE, waiting=True
    # )
    br.turnInPlace(angle=-80, speedPct=45, then=Stop.BRAKE, waiting=False)
    br.moveLeftAttachmentMotorForDegrees(degrees=900, speedPct=80)
    br.driveForDistance(
        distance=230, speedPct=80, then=Stop.BRAKE, waiting=True
    )

    br.moveRightAttachmentMotorForDegrees(
        degrees=370, speedPct=40, waiting=False
    )
    br.moveLeftAttachmentMotorForDegrees(degrees=-900, speedPct=80)
    br.moveLeftAttachmentMotorForDegrees(degrees=600, speedPct=80)
    br.moveRightAttachmentMotorForDegrees(degrees=-300, speedPct=40)
    br.driveForDistance(
        distance=-220, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveLeftAttachmentMotorForDegrees(degrees=-600, speedPct=80)
    br.driveArcDist(
        radius=50, dist=100, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.driveArcDist(
        radius=-700, dist=500, speedPct=80, then=Stop.BRAKE, waiting=True
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
