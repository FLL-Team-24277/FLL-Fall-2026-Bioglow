from base_robot import *

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
        distance=100, speedPct=80, then=Stop.BRAKE, waiting=True
    )

    # dfm
    br.driveForMillis(millis=4000, speedPct=80)

    # tip
    br.turnInPlace(90)

    # rmd
    br.moveRightAttachmentMotorForDegrees(degrees=700, speedPct=80)

    # rmm
    br.moveRightAttachmentMotorForMillis(millis=7000, speedPct=80)

    # lmd
    br.moveLeftAttachmentMotorForDegrees(degrees=600, speedPct=80)

    # lmm
    br.moveLeftAttachmentMotorForMillis(millis=6000, speedPct=80)

    # dad
    br.driveArcDist(
        radius=1000, dist=400, speedPct=80, then=Stop.BRAKE, waiting=True
    )

    # cur
    br.curve(radius=1500, angle=70, speedPct=80, then=Stop.BRAKE, waiting=True)

    # wbb
    br.waitForBackButton()

    # wfb
    br.waitForForwardButton()

    # lms
    br.moveLeftAttachmentMotorUntilStalled(speedPct=80, stallPct=50)

    # rms
    br.moveRightAttachmentMotorUntilStalled(speedPct=80, stallPct=50)

    # wfm
    br.waitForMillis(millis=5000)


# Leave everything below here and don't type anything below this line
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
