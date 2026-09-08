from base_robot import *


# left side BLUE
# Simple test mission: wait for the forward button, then drive forward,
# turn, and drive again. This gives you a predictable pattern for tuning.
# When we run this program from the master program, we will call this
def Run(br: BaseRobot):
    br.driveForDistance(
        distance=800,
        speedPct=80,
        then=Stop.BRAKE,
        waiting=True,
    )
    br.turnInPlace(angle=90, speedPct=45)
    br.driveForDistance(
        distance=1000, speedPct=80, then=Stop.BRAKE, waiting=True
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
