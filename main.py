######################################################
### Projekt: Pilot-ZiRa ---Slave---                ###
### Version: 1.01                                  ###
### Datum  : 25.11.2025                            ###
######################################################
#from machine import Pin, Timer                              # type: ignore
from libs.module_init import Global_Module as MyModule
from time import sleep                                       # type: ignore

TIME_LOOP = 0.3

COLOR_OFF       = (  0,  0,  0)
COLOR_RED       = ( 80,  0,  0)
COLOR_GREEN     = (  0, 80,  0)
COLOR_BLUE      = (  0,  0, 80)
COLOR_YELLOW    = ( 50, 50,  0)
COLOR_DEFAULT   = (  0,  0,  2)

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------

def main():

    print("=== Main ===")
    
    try:
        print("Start Main Loop")

        xio = MyXIO.XIO("INPUT")

        led_1 = MyWS2812.LED_STRIP(20, 0, 2, COLOR_RED, COLOR_YELLOW, True, "Mask")

        led_1.led_gradient()
        led_1.led_show()

 
        while (True):
            
            print(hex(xio.read_io()))

            if xio.get_bit(0):
                pass
            else:
                pass
            
            sleep(TIME_LOOP)


    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    finally:
        print("Exiting the program")   

    print("=== End of Main ===")

# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################

if __name__ == "__main__":

    print("=== Pilot-ZiRa-Slave ===")
    
    if MyModule.inc_ws2812:
        print("Wird geladen -> Modul WS2812")
        import libs.module_ws2812_v3 as MyWS2812
    else:
        print("Nicht genutzt -> Modul WS2812")

    if MyModule.inc_xio:
        print("XIO -> Load-Module")
        import libs.module_xio as MyXIO
    else:
        print("XIO -> nicht vorhanden")

    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___ End of Programm ___")
print("--> !!! STOP !!! <---")

# ##############################################################################
