######################################################
### Projekt: Pilot-ZiRa ---Slave---                ###
### Version: 1.01                                  ###
### Datum  : 13.11.2025                            ###
######################################################
#from machine import Pin, Timer                              # type: ignore
from libs.module_init import Global_Module as MyModule
from time import sleep                                       # type: ignore

TIME_LOOP = 0.3

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------

def main():

    print("=== Main ===")
    
    try:
        print("Start Main Loop")

        xio = MyXIO.XIO("INPUT")
 
        while (True):
            
            print(hex(xio.read_io()))

            MyWS2812.set_led_obj(3, "def")
            
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
        import libs.module_ws2812_v2 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        #print("WS2812 -> Setup")
        MyWS2812.setup_ws2812()
        ### Test ###
        print("WS2812 -> Run self test")
        MyWS2812.self_test()
        print("WS2812 -> Blink Test")
        #MyWS2812.do_blink_test()
        #print("WS2812 -> Dot-Test")
        #MyWS2812.do_dot_test()
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
