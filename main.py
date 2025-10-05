######################################################
### Projekt: Pilot ZiRa                            ###
### Version: Slave                                 ###
### Datum  : 05.10.2025                            ###
######################################################
#from machine import Pin, Timer                              # type: ignore
from libs.module_init import Global_Module as MyModule
from time import sleep                                                 # type: ignore

TIME_LOOP = 0.3

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------

def main():

    print("=== Main ===")
    
    try:
        print("Start Main Loop")
 
        while (True):
            
            sleep(TIME_LOOP)

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    finally:
        print("Exiting the program")   

    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################

if __name__ == "__main__":

    print("=== Pilot-ZiRa-Slave ===")
    if MyModule.inc_i2c:
        print("Wird geladen -> Modul I2C")
        import libs.module_i2c as MyGPIO
        #print("I2C -> Setup")
        MyGPIO.i2c_setup()
        ### Test ###
        print("I2C -> SetOutput")
        MyGPIO.i2c_write(0,True)
        time.sleep(0.5)
        MyGPIO.i2c_write(0,False)
    else:
        print("Nicht genutzt -> Modul I2C")

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

    if MyModule.inc_decoder:
        print("Decode -> Load-Module")
        import libs.module_decode as MyDecode
        #print("Decode -> Setup")
        MyDecode.decode_setup()
        ### Test ###
        #print("Decode -> Test")
        #MyDecode.decode_input("Test")
    else:
        print("Decode -> nicht vorhanden")

    if MyModule.inc_serial:
        print("Serial-COM -> Load-Module")
        import libs.module_serial as MySerial
        #print("Serial-Con -> Setup")
        MySerial.sercon_setup()
        ### Test ###
        #print("Serial-Con -> Test")
        #MySerial.sercon_write_out("Start Test")
    else:
        print("Serial-COM -> nicht vorhanden")

    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___ End of Programm ___")
print("--> !!! STOP !!! <---")

# ##############################################################################
