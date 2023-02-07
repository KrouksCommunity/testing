import subprocess
import re

def MonitorMode(interface, state):
    if state == "on":
        subprocess.run(["sudo", "ifconfig", interface, "down"])
        subprocess.run(["sudo", "iwconfig", interface, "mode", "monitor"])
        subprocess.run(["sudo", "ifconfig", interface, "up"])
        print("[+] Monitor mode enabled")
    elif state == "off":
        subprocess.run(["sudo", "ifconfig", interface, "down"])
        subprocess.run(["sudo", "iwconfig", interface, "mode", "managed"])
        subprocess.run(["sudo", "ifconfig", interface, "up"])
        print("[-] Monitor mode disabled")

def ListInterfaces():
    result = subprocess.run(["ifconfig"], stdout=subprocess.PIPE)
    output = result.stdout.decode("utf-8")
    interfaces = re.findall(r'^(\w+)\s', output, re.MULTILINE)
    print("[+] List of network interfaces:")
    for i in interfaces:
        print(i)


def main():
    while True:
        print("1. Monitor mode (on/off)")
        print("2. List network interfaces")
        print("3. Quit")

        try:
            option = int(input("Enter option number: "))
        except ValueError:
            print("Invalid option, please enter a valid number")
            continue

        if option == 1:
            interface = input("Enter network interface: ")
            state = input("Turn on (on) or off (off) monitor mode?\n")
            MonitorMode(interface, state)
        elif option == 2:
            ListInterfaces()
        elif option == 3:
            print("Quitting...")
            break
        else:
            print("Invalid option, try again")


if __name__ == "__main__":
    main()
