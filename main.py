######################################################
### Projekt: Pilot-ZiRa ---Slave---                ###
### Version: 1.01                                  ###
### Datum  : 25.11.2025                            ###
######################################################
#from machine import Pin, Timer                              # type: ignore
from libs.module_init import Global_Module as MyModule
#from libs.module_init import Global_WS2812 as MyGlobal
from time import sleep                                       # type: ignore

TIME_LOOP   = 0.1
TIME_DELAY  = 10

COLOR_OFF       = (  0,  0,  0)
COLOR_RED       = ( 70,  0,  0)
COLOR_RED_2     = ( 20,  0,  0)
COLOR_GREEN     = (  0, 70,  0)
COLOR_GREEN_2   = (  0, 20,  0)
COLOR_BLUE      = (  0,  0, 70)
COLOR_YELLOW    = ( 50, 50,  0)
COLOR_DEFAULT   = (  0,  0,  2)

NUMPIX_1        = 26        # Anz. LEDs im 1. Stripe -> 
NUMPIX_2        = 54        # Anz. LEDs im 2. Stripe -> 
NUMPIX_3        = 48        # Anz. LEDs im 3. Stripe -> 
NUMPIX_4        = 42        # Anz. LEDs im 4. Stripe -> 
NUMPIX_5        = 48        # Anz. LEDs im 5. Stripe -> 
NUMPIX_6        = 64        # Anz. LEDs im 6. Stripe -> 
NUMPIX_7        = 52        # Anz. LEDs im 7. Stripe -> 
NUMPIX_8        = 109       # Anz. LEDs im 8. Stripe -> 

def set_all_gradient(stripes):
    for led in stripes:
        led.led_gradient()
    show_all(stripes)

def set_all_stripes(stripes, color):
    for led in stripes:
        led.set_color_value(color)
        led.led_fill()
    show_all(stripes)

def anim_all(stripes):
    for led in stripes:
        led.make_anim()
    show_all(stripes)

def reset_anim(stripes):
    for led in stripes:
        led.anim_count  = 0
        led.anim_offset = 0

def show_all(stripes):
    for led in stripes:
        led.led_show()

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------

def main():

    print("=== Main ===")
    
    try:
        print("Start Main Loop")

        xio = MyXIO.XIO("INPUT")

        led_1 = MyWS2812.LED_STRIP(NUMPIX_1, 0, 2, COLOR_RED, COLOR_RED, COLOR_DEFAULT, True, 2)          # Nutzwärme Austritt
        led_2 = MyWS2812.LED_STRIP(NUMPIX_2, 1, 3, COLOR_YELLOW, COLOR_YELLOW, COLOR_DEFAULT, True, 2)    # Nutzwärem Eintritt
        led_3 = MyWS2812.LED_STRIP(NUMPIX_3, 2, 4, COLOR_RED, COLOR_YELLOW, COLOR_DEFAULT, True, 2)       # Kondensator
        led_4 = MyWS2812.LED_STRIP(NUMPIX_4, 3, 5, COLOR_BLUE, COLOR_BLUE, COLOR_DEFAULT, True, 2)        # Abwärme Austritt
        led_5 = MyWS2812.LED_STRIP(NUMPIX_5, 4, 6, COLOR_YELLOW, COLOR_BLUE, COLOR_DEFAULT, False, 2)     # Drossel           -> Richtung anpassen
        led_6 = MyWS2812.LED_STRIP(NUMPIX_6, 5, 7, COLOR_BLUE, COLOR_YELLOW, COLOR_DEFAULT, True, 2)      # Verdampfer
        led_7 = MyWS2812.LED_STRIP(NUMPIX_7, 6, 8, COLOR_YELLOW, COLOR_YELLOW, COLOR_DEFAULT, False, 2)   # Abwärme Eintritt  -> Richtung anpassen
        led_8 = MyWS2812.LED_STRIP(NUMPIX_8, 7, 9, COLOR_YELLOW, COLOR_RED, COLOR_DEFAULT, True, 2)       # Kompressor 1 und Kompressor 2

        all_leds = [led_1, led_2, led_3, led_4, led_5, led_6, led_7, led_8]

        set_all_stripes(all_leds, COLOR_OFF)

        wait_0 = 0
        wait_1 = 0
        wait_2 = 0

        while (True):
            
            io_state = xio.read_io()
            if io_state == 0:
                wait_1 = 0
                wait_2 = 0
                if wait_0 < TIME_DELAY:
                    set_all_stripes(all_leds, COLOR_OFF)
                    reset_anim(all_leds)
                    wait_0 += 1
                else:
                    set_all_stripes(all_leds, COLOR_DEFAULT)
            if io_state == 1:
                wait_0 = 0
                wait_2 = 0
                if wait_1 < TIME_DELAY:
                    set_all_stripes(all_leds, COLOR_GREEN_2)
                    wait_1 += 1
                else:
                    anim_all(all_leds)
            if io_state == 2:
                wait_0 = 0
                wait_1 = 0
                if wait_2 < TIME_DELAY:
                    set_all_stripes(all_leds, COLOR_RED_2)
                    led_2.color_start   = COLOR_RED
                    led_2.color_stop    = COLOR_RED
                    led_3.color_start   = COLOR_RED
                    led_3.color_stop    = COLOR_RED
                    wait_2 += 1
                else:
                    led_2.make_anim()
                    led_3.make_anim()
                    led_2.led_show()
                    led_3.led_show()
            
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
