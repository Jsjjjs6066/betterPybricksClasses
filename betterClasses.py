from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks._common import MaybeAwaitable
from typing import Optional, Union, Collection

class BetterMotor(Motor):
    def __init__(self, port: Port, default_speed: Union[int, float], positive_direction: Direction = Direction.CLOCKWISE, gears: Optional[Union[Collection[int], Collection[Collection[int]]]] = None, reset_angle: bool = True, profile: Union[None, Union[int, float]] = None) -> None:
        self.default_speed = default_speed
        super().__init__(port, positive_direction, gears, reset_angle, profile)
    def run_target(self, angle: Union[int, float], speed: Union[None, Union[int, float]] = None, then: Stop = Stop.HOLD, wait: bool = True) -> MaybeAwaitable:
        if speed is None:
            super().run_target(self.default_speed, angle, then, wait)
        else:
            super().run_target(speed, angle, then, wait)
    def run_angle(self, angle: Union[int, float], speed: Union[None, Union[int, float]] = None, then: Stop = Stop.HOLD, wait: bool = True) -> MaybeAwaitable:
        if speed is None:
            super().run_angle(self.default_speed, angle, then, wait)
        else:
            super().run_angle(speed, angle, then, wait)

class BetterDriveBase(DriveBase):
    def __init__(self, left_motor: Motor, right_motor: Motor, wheel_diameter: Union[int, float], axle_track: Union[int, float]) -> None:
        super().__init__(left_motor, right_motor, wheel_diameter, axle_track)
    def drive(self, speed: Union[int, float], turn_rate: Union[int, float] = 0) -> None:
        super().drive(speed, turn_rate)