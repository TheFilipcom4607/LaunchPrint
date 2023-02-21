import sys

try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        sys.exit("error loading launchpad.py")

print("enter what you want to print on ur launchpad:")
x = input()

def main():
    mode = None

    # create an instance for the Pro
    if launchpad.LaunchpadPro().Check(0):
        lp = launchpad.LaunchpadPro()
        if lp.Open(0):
            print("Printing on: Launchpad Pro")
            mode = "Pro"

    elif launchpad.LaunchpadProMk3().Check(0):
        lp = launchpad.LaunchpadProMk3()
        if lp.Open(0):
            print("Printing on: Launchpad Pro Mk3")
            mode = "ProMk3"

    # experimental MK3 implementation
    # The MK3 has two MIDI instances per device; we need the 2nd one.
    # If you have two MK3s attached, its "1" for the first and "3" for the 2nd device
    elif launchpad.LaunchpadMiniMk3().Check(1):
        lp = launchpad.LaunchpadMiniMk3()
        if lp.Open(1, "minimk3"):
            print("Printing on: Launchpad Mini Mk3")
            mode = "Pro"

    # experimental LPX implementation
    # Like the Mk3, the LPX also has two MIDI instances per device; we need the 2nd one.
    # If you have two LPXs attached, its "1" for the first and "3" for the 2nd device
    elif launchpad.LaunchpadLPX().Check(1):
        lp = launchpad.LaunchpadLPX()
        if lp.Open(1, "lpx"):
            print("Printing on: Launchpad X")
            mode = "Pro"

    elif launchpad.LaunchpadMk2().Check(0):
        lp = launchpad.LaunchpadMk2()
        if lp.Open(0, "mk2"):
            print("Printing on: Launchpad Mk2")
            mode = "Mk2"

    elif launchpad.LaunchControlXL().Check(0):
        lp = launchpad.LaunchControlXL()
        if lp.Open(0, "control xl"):
            print("Printing on: Launch Control XL")
            mode = "XL"

    elif launchpad.LaunchKeyMini().Check(0):
        lp = launchpad.LaunchKeyMini()
        if lp.Open(0, "launchkey"):
            print("Printing on: LaunchKey (Mini)")
            mode = "LKM"

    elif launchpad.Dicer().Check(0):
        lp = launchpad.Dicer()
        if lp.Open(0, "dicer"):
            print("Printing on: Dicer")
            mode = "Dcr"

    elif launchpad.MidiFighter64().Check(0):
        lp = launchpad.MidiFighter64()
        if lp.Open(0):
            print("Printing on: Midi Fighter 64")
            mode = "MF64"

    else:
        lp = launchpad.Launchpad()
        if lp.Open():
            print("Printing on: Launchpad Mk1/S/Mini")
            mode = "Mk1"

    if mode is None:
        print("Did not find any Launchpads, meh...")
        return

    # scroll a string from right to left
    if mode == "Mk1":
        lp.LedCtrlString("UWU", 0, 3, -1)
    # the MF64's methods are not compatible with the Launchpad ones
    elif mode == "MF64":
        lp.LedCtrlString("UWU", 5, 0, -1, waitms=50)
    # for all others except the XL and the LaunchKey
    elif mode != "XL" and mode != "LKM" and mode != "Dcr":
        lp.LedCtrlString(x, 0, 63, 0, -1, waitms=50)


    # now quit...


    lp.Reset()  # turn all LEDs off
    lp.Close()  # close the Launchpad (will quit with an error due to a PyGame bug)


if __name__ == '__main__':
    main()
