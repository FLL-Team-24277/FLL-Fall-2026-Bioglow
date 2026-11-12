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
        radius=158,
        dist=135,
        speedPct=100,
        then=Stop.NONE,
        waiting=True,
        accelerationPct=55,
    )

    # Appoach the exploding seeds
    br.driveForDistance(
        distance=255,
        speedPct=100,
        then=Stop.BRAKE,
        waiting=True,
        accelerationPct=55,
    )

    # Raise the tray to pick up the exploding seeds
    br.moveLeftAttachmentMotorForMillis(millis=145, speedPct=100)

    # Backup after picking up the exploding seeds
    br.driveForDistance(
        distance=-210,
        speedPct=100,
        then=Stop.BRAKE,
        waiting=True,
        accelerationPct=48,
    )

    br.moveLeftAttachmentMotorForMillis(millis=92, speedPct=-100)
    br.driveArcDist(
        radius=450,
        dist=275,
        speedPct=100,
        then=Stop.NONE,
        waiting=True,
        accelerationPct=40,
    )
    br.turnInPlace(angle=-17, speedPct=80)
    br.driveArcDist(
        radius=230,
        dist=85,
        speedPct=100,
        then=Stop.NONE,
        waiting=True,
        accelerationPct=40,
    )
    br.driveForDistance(
        distance=140,
        speedPct=80,
        then=Stop.BRAKE,
        waiting=True,
        accelerationPct=48,
    )

    br.moveRightAttachmentMotorForMillis(millis=1100, speedPct=120)
    wait(690)
    br.moveLeftAttachmentMotorForMillis(millis=90, speedPct=-100)
    br.moveRightAttachmentMotorForMillis(millis=1100, speedPct=-100)
    br.driveArcDist(
        radius=-730,
        dist=135,
        speedPct=100,
        then=Stop.NONE,
        waiting=True,
        accelerationPct=48,
    )
    br.driveForDistance(
        distance=132,
        speedPct=100,
        then=Stop.BRAKE,
        waiting=True,
        accelerationPct=48,
    )
    br.moveLeftAttachmentMotorForDegrees(degrees=100, speedPct=15)
    br.driveForDistance(
        distance=-120,
        speedPct=100,
        then=Stop.BRAKE,
        waiting=True,
        accelerationPct=48,
    )
    br.moveLeftAttachmentMotorForMillis(millis=245, speedPct=-20)
    br.driveForDistance(
        distance=1,
        speedPct=100,
        then=Stop.NONE,
        waiting=True,
        accelerationPct=48,
    )
    br.driveArcDist(
        radius=430,
        dist=300,
        speedPct=100,
        then=Stop.NONE,
        waiting=True,
        accelerationPct=40,
    )
    br.driveForDistance(
        distance=800,
        speedPct=100,
        then=Stop.NONE,
        waiting=True,
        accelerationPct=100,
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
