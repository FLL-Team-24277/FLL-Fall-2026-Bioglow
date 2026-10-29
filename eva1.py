from base_robot import *


# leftLUE
# Sie tesssion: waitherward button, then drive forward,
# turn, and drigain. This g you a predictaattern for tuning.
# When we runis program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Wait until the team is ready and the robot is in its starting position.
    br.driveForDistance(
        distance=500,
        speedPct=100,
        then=Stop.BRAKE,
        waiting=True,
    )

    br.driveForDistance(
        distance=-200,
        speedPct=100,
        then=Stop.BRAKE,
        waiting=True,
    )


# Leave everything below here and don't type anything below this line.
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
