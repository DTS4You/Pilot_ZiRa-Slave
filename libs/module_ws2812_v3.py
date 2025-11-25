###############################################################################
### WS2812 Animation
### Version: 0.99
###############################################################################
import time
from libs.neopixel import Neopixel




class LED_STRIP:
    def __init__(self, num_pix, pio_num, pin_num, color_start, color_stop, color_default, direction, anim_type, brightness, transfer_mode="PUT"):
        self.num_pix        = num_pix 
        self.pio_num        = pio_num 
        self.pin_num        = pin_num
        self.transfer       = transfer_mode
        self.color_default  = color_default
        self.color_start    = color_start
        self.color_stop     = color_stop
        self.color_value    = ( 40, 40, 40)
        self.color_off      = (  0,  0,  0)
        self.anim_count     = 0
        self.anim_enable    = True
        self.anim_pattern   = 3
        self.anim_offset    = 0
        self.anim_type      = anim_type
        self.direction      = direction
        self.offset         = 8
        self.bright         = brightness

        self.led_setup()

    def set_color_default(self, color):
        self.color_default = color
    
    def set_color_value(self, color):
        self.color_value = color

    def led_setup(self):
        self.strip = (Neopixel(self.num_pix, self.pio_num, self.pin_num, "GRB", 0.0001, self.transfer))

    def led_set_pixel(self):
        self.strip.set_pixel(self.anim_count, self.color_value)

    def led_fill(self):
        self.strip.fill(self.color_value)

    def led_gradient(self):
        self.strip.set_pixel_line_gradient(0, self.num_pix - 1, self.color_start, self.color_stop)

    def led_show(self):
        self.strip.show()

    def anim_step(self):
        if self.anim_enable:
            if self.direction:
                if self.anim_count < self.num_pix - 1:
                    self.anim_count += 1
                else:
                    self.anim_count = 0
                
                if self.anim_offset < self.anim_pattern:
                    self.anim_offset += 1
                else:
                    self.anim_offset = 0
            else:
                if self.anim_count > 0:
                    self.anim_count -= 1
                else:
                    self.anim_count = self.num_pix - 1

                if self.anim_offset > 0:
                    self.anim_offset -= 1
                else:
                    self.anim_offset = self.anim_pattern

    def mask_stripe(self):
        self.led_gradient()
        if self.anim_count > 0:
            self.strip.set_pixel_line(0, self.anim_count - 1 , self.color_default)
        if self.anim_count < self.num_pix - self.offset - 1:
            self.strip.set_pixel_line(self.anim_count + self.offset, self.num_pix, self.color_default)
    
    def dim_stripes(self):
        for i in range(0,self.num_pix, 4):
            if i + self.anim_pattern < self.num_pix: 
                self.strip.set_pixel(i + self.anim_offset, self.strip.get_pixel(i), self.bright)

    def make_anim(self):
        if self.anim_type == 0:
            self.led_fill()
            self.led_set_pixel()
        if self.anim_type == 1:
            self.led_gradient()
            self.mask_stripe()
        if self.anim_type == 2:
            self.led_gradient()
            self.dim_stripes()
        self.anim_step()


# -----------------------------------------------------------------------------

def main():

    COLOR_OFF       = (  0,  0,  0)
    COLOR_RED       = ( 80,  0,  0)
    COLOR_GREEN     = (  0, 80,  0)
    COLOR_BLUE      = (  0,  0, 80)
    COLOR_YELLOW    = ( 50, 50,  0)
    COLOR_DEFAULT   = (  0,  0,  2)
    
    led_1 = LED_STRIP(20, 0, 2, COLOR_RED, COLOR_YELLOW, COLOR_DEFAULT, True, 2, 30)


    led_1.led_gradient()
    led_1.led_show()
 

    time.sleep(1)

    while(True):
        led_1.make_anim()
        led_1.led_show()
        time.sleep(0.3)

# End

#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
