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

    # Reset the tray initially to make sure it is in the right position
    br.moveLeftAttachmentMotorForMillis(millis=125, speedPct=100)
    br.driveArcDist(
        radius=157, dist=135, speedPct=100, then=Stop.NONE, waiting=True
    )

    # Appoach the exploding seeds
    br.driveForDistance(
        distance=255, speedPct=100, then=Stop.BRAKE, waiting=True
    )

    # Raise the tray to pick up the exploding seeds
    br.moveLeftAttachmentMotorForMillis(millis=145, speedPct=100)

    # Backup after picking up the exploding seeds
    br.driveForDistance(
        distance=-210, speedPct=100, then=Stop.BRAKE, waiting=True
    )

    br.moveLeftAttachmentMotorForMillis(millis=92, speedPct=-100)
    br.driveArcDist(
        radius=450, dist=275, speedPct=100, then=Stop.NONE, waiting=True
    )
    br.turnInPlace(angle=-20, speedPct=80)
    br.driveArcDist(
        radius=300, dist=125, speedPct=100, then=Stop.NONE, waiting=True
    )
    br.driveForDistance(
        distance=133, speedPct=80, then=Stop.BRAKE, waiting=True
    )

    br.moveRightAttachmentMotorForMillis(millis=1420, speedPct=120)
    wait(890)
    br.moveLeftAttachmentMotorForMillis(millis=90, speedPct=-100)
    br.moveRightAttachmentMotorForMillis(millis=1420, speedPct=-100)
    br.driveArcDist(
        radius=-840, dist=135, speedPct=100, then=Stop.NONE, waiting=True
    )
    br.driveForDistance(
        distance=133, speedPct=100, then=Stop.BRAKE, waiting=True
    )
    br.moveLeftAttachmentMotorForDegrees(degrees=90, speedPct=100)
    br.driveForDistance(
        distance=-120, speedPct=100, then=Stop.BRAKE, waiting=True
    )
    br.moveLeftAttachmentMotorForMillis(millis=200, speedPct=-20)
    br.driveForDistance(distance=1, speedPct=100, then=Stop.NONE, waiting=True)
    br.driveArcDist(
        radius=100, dist=10, speedPct=100, then=Stop.NONE, waiting=True
    )
    br.driveForDistance(
        distance=36, speedPct=100, then=Stop.NONE, waiting=True
    )
    br.driveArcDist(
        radius=80, dist=50, speedPct=100, then=Stop.BRAKE, waiting=True
    )
    br.driveForDistance(
        distance=850, speedPct=100, then=Stop.BRAKE, waiting=True
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
