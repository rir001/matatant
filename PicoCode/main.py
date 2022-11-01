from machine import Pin, UART, PWM

uart = UART(0,9600)

class Wheel:
    def __init__(self, pin1:int, pin2:int, max:int):
        self.front = PWM(Pin(pin1))
        self.front.freq(1000)

        self.back  = PWM(Pin(pin2))
        self.back.freq(1000)

        self.max_vel = max

        self._velocidad = 0

    @property
    def vel(self):
        return self._velocidad

    @vel.setter
    def vel(self, change):
        if change > 100:
            self._velocidad = 100
        elif change < -100:
            self._velocidad = -100
        else:
            self._velocidad = change

        if self._velocidad < 0:
            self.front.duty_u16(0)
            self.back.duty_u16(int(self.max_vel - self.max_vel * self._velocidad/100))

        elif self._velocidad > 0:
            self.back.duty_u16(0)
            self.front.duty_u16(int(self.max_vel * self._velocidad/100))

        elif self._velocidad == 0:
            self.front.duty_u16(0)
            self.back.duty_u16(0)



WL = Wheel(2, 3, 67000)
WR = Wheel(4, 5, 100000)


run = 1

while run:
    command = ''
    if uart.any():
        char = uart.readline().decode("utf-8") # type: ignore
        if char == '$':
            char = ''
            while char != '$':
                if uart.any():
                    command += char
                    char = uart.readline().decode("utf-8")  # type: ignore
        else:
            command = char

    if '%' in command:
        print(command, command.split('%'))
        command = command.split('%')

        if command[0] == 'L':
            WL.vel = int(command[1])
        if command[0] == 'R':
            WR.vel = int(command[1])
        if command[0] == 'A':
            WL.vel = int(command[1])
            WR.vel = int(command[1])

        print(f'velocidad R: {WR.vel} || velocidad L: {WL.vel}')

    elif '!' in command:
        run = 0

