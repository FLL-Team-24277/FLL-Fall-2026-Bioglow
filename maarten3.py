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

    br.driveArcDist(
        radius=-280,
        dist=-202,
        speedPct=80,
        then=Stop.BRAKE,
        waiting=True,
        accelerationPct=40,
    )
    br.driveForDistance(
        distance=300, speedPct=80, then=Stop.NONE, waiting=True
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
