class PIDController:
    def __init__(self, kp, ki, kd, setpoint=0, output_limits=(0, 180)):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.output_limits = output_limits
        self._last_error = 0
        self._integral = 0
    def update(self, measurement, dt):
        error = self.setpoint - measurement
        self._integral += error * dt
        derivative = (error - self._last_error) / dt if dt > 0 else 0
        output = self.kp * error + self.ki * self._integral + self.kd * derivative
        output = max(self.output_limits[0], min(self.output_limits[1], output))
        self._last_error = error
        return output

if __name__ == '__main__':
    import time
    pid = PIDController(1.0, 0.1, 0.05, setpoint=100)
    measurement = 0
    for _ in range(20):
        dt = 0.1
        output = pid.update(measurement, dt)
        print(f'PID output: {output}')
        measurement += output * dt
        time.sleep(dt) 