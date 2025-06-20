from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right = Motor(Port.A)
hand: Motor = Motor(Port.C)

db: DriveBase = DriveBase(left, right, 62.4, 129)

def main() -> None:
    pass

if __name__ == "__main__":
    main()