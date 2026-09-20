from components.driving_direction import DrivingDirection

class CoordinateDirection:
    X_PLUS = "X"    
    X_MINUS = "-X"
    Y_PLUS = "Y"
    Y_MINUS = "-Y"

    def __init__(self):
        self.current_coordinate_direction = CoordinateDirection.Y_PLUS

    def set_present_coordinate_direction(self, direction):
        if self.current_coordinate_direction == CoordinateDirection.Y_PLUS:
            if direction == DrivingDirection.FORWARD:
                pass
            elif direction == DrivingDirection.LEFT:
                self.current_coordinate_direction = CoordinateDirection.X_MINUS
            elif direction == DrivingDirection.RIGHT:
                self.current_coordinate_direction = CoordinateDirection.X_PLUS
            elif direction == DrivingDirection.BACKWARD:
                self.current_coordinate_direction = CoordinateDirection.Y_MINUS
        if self.current_coordinate_direction == CoordinateDirection.Y_MINUS:
            if direction == DrivingDirection.BACKWARD:
                self.current_coordinate_direction = CoordinateDirection.Y_MINUS
            elif direction == DrivingDirection.LEFT:
                self.current_coordinate_direction = CoordinateDirection.X_MINUS
            elif direction == DrivingDirection.RIGHT:
                self.current_coordinate_direction = CoordinateDirection.X_PLUS
            elif direction == DrivingDirection.FORWARD:
                pass
        if self.current_coordinate_direction == CoordinateDirection.X_MINUS:
            if direction == DrivingDirection.LEFT:
                self.current_coordinate_direction = CoordinateDirection.X_MINUS
            elif direction == DrivingDirection.BACKWARD:
                self.current_coordinate_direction = CoordinateDirection.Y_MINUS
            elif direction == DrivingDirection.RIGHT:
                self.current_coordinate_direction = CoordinateDirection.X_PLUS
            elif direction == DrivingDirection.FORWARD:
                pass
        if self.current_coordinate_direction == CoordinateDirection.X_PLUS:
            if direction == DrivingDirection.RIGHT:
                self.current_coordinate_direction = CoordinateDirection.X_PLUS
            elif direction == DrivingDirection.LEFT:
                self.current_coordinate_direction = CoordinateDirection.X_MINUS
            elif direction == DrivingDirection.FORWARD:
                pass
            elif direction == DrivingDirection.BACKWARD:
                self.current_coordinate_direction = CoordinateDirection.Y_MINUS