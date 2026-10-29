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
    # br.driveArcDist(
    #     radius=150, dist=-300, speedPct=80, then=Stop.BRAKE, waiting=True
    # )
    # br.driveForDist?ance(
    #     distance=125,
    #     speedPct=100,
    #     then=Stop.BRAKE,
    #     waiting=True,
    #     accelerationPct=100,
    # )

    br.driveForDistance(
        distance=740,
        speedPct=80,
        then=Stop.BRAKE,
        waiting=True,
        accelerationPct=90,
    )
    # br.moveLeftAttachmentMotorForDegrees(degrees=200, speedPct=80)
    # br.driveForDistance(
    #     distance=140, speedPct=80, then=Stop.BRAKE, waiting=True
    # )
    br.moveRightAttachmentMotorForDegrees(degrees=-165, speedPct=80)
    # br.driveForDistance(
    #     distance=-100, speedPct=80, then=Stop.BRAKE, waiting=True
    # )
    # br.moveRightAttachmentMotorForDegrees(degrees=70, speedPct=80)
    br.driveForDistance(
        distance=-100,
        speedPct=80,
        then=Stop.BRAKE,
        waiting=True,
        accelerationPct=80,
    )
    br.driveForDistance(
        distance=70, speedPct=100, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForDegrees(degrees=150, speedPct=80)
    # br.moveLeftAttachmentMotorForDegrees(degrees=-200, speedPct=80)
    br.turnInPlace(angle=-90, speedPct=15)
    br.driveForDistance(
        distance=300, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.turnInPlace(angle=-45, speedPct=45)
    br.driveForDistance(
        distance=-180, speedPct=10, then=Stop.BRAKE, waiting=True
    )
    br.driveArcDist(
        radius=-500, dist=1200, speedPct=80, then=Stop.BRAKE, waiting=True
    )


# br.moveLeftAttachmentMotorForMillis(millis=1000, speedPct=-100)
# br.turnInPlace(angle=30, speedPct=25)
# br.driveArcDist(
#     radius=400, dist=600, speedPct=100, then=Stop.BRAKE, waiting=True
# )
# br.turnInPlace(angle=50, speedPct=45)
# br.driveForDistance(
# distance=-700, speedPct=80, then=Stop.BRAKE, waiting=True
# )


# Leave everything below here and don't type anything below this line
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
