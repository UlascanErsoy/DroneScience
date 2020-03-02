from time import sleep
import LocoDrone
import platform
import serial
usb_port_address = "COM3"

def availableSerialPorts():
        """Windows Only"""
        if platform.system() != "Windows":
                print("Available Ports Feature is only implemented for Windows!\nYou're going to have to check available ports manually!")
                return []
        maxPorts = ["COM{}".format(a) for a in range(256)]
        res = []
        for port in maxPorts:
                try:
                        s = serial.Serial(port)
                        s.close()
                        res.append(port)
                except:
                        pass
        return res

DATA = []

if __name__ == "__main__":
        ports = availableSerialPorts()
        print("Press Ctrl-C to Exit!")
        print("Available Ports Are: ",end="")
        print(",".join(ports))
        usb_port_address = input("Choose Port: ")
        loco_drone = LocoDrone.LocoDrone()
        loco_drone.connect(usb_port_address)

        loco_drone.set_mode(loco_drone.MODE_JOYSTICK)
        loco_drone.controller_calibrate()
        loco_drone.drone_calibrate()
        try:
                while True:
                        loco_drone.read_data(loco_drone.DRONE_DATA)
                        loco_drone.read_data(loco_drone.ACCELEROMETER)
                        loco_drone.read_data(loco_drone.GYROSCOPE)
                        r = (f'{loco_drone.ax:.2f}', f'{loco_drone.ay:.2f}', f'{loco_drone.az:.2f}')
                        DATA.append(r)
                        print("x:{} , y:{} , z:{}".format(r[0],r[1],r[2]))
                sleep(0.25)
        except KeyboardInterrupt:
                print("Quitting Program!")
                q = input("Would you like to save the data to a csv file?(y/n)")
                if "y" in q:
                        f_name = input("Enter file name: ")
                        csv = "Accel(x) , Accel(y) , Accel(z)\n"
                        for row in DATA:
                                csv += "{},{},{}".format(row[0],row[1],row[2])+"\n"
                        open(f_name,"w").write(csv)
