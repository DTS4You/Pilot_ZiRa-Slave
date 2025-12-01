class PLC:
    def __init__(self):
        self.state_now      = 'NONE'           # Aktueller Zustand der Steuerung
        self.state_last     = 'NONE'           # Letzter Zustand der Steuerung
        self.state_change   = False
        self.autostart      = False
        self.step_max = 5                   # Maximale Schritte Anzahl
        self.inputs = {                     # Eingänge (z.B. Taster, Sensoren)
            'TASTER_HINTEN': False,
            'TASTER_VORNE': False,
            'KONTAKT_ROT': False,
            'KONTAKT_GRUEN': False
        }
        self.outputs = {                    # Ausgänge (z.B. Motor, Relais)
            'TASTER_HINTRN_ROT': False,
            'TASTER_HINTEN_GRUEN': False,
            'TASTER_VORNE_ROT': False,
            'TASTER_VORNE_GRUEN': False,
            'KESSEL_LED_1': False,
            'KESSEL_LED_2': False,
            'WINDRAD': False,
            'TUER_KLAPPE': False
        }

        self.setup_state()

    def setup_state(self):
        if self.autostart:
            self.state_now = 'START'
            self.state_change = True

    def read_input(self):
        # Eingänge einlesen und auf Merker setzen
        self.inputs['start'] = input("Start-Taster drücken? (ja/nein): ").lower() == 'ja'
        self.inputs['stop'] = input("Stop-Taster drücken? (ja/nein): ").lower() == 'ja'
        self.inputs['sensor'] = input("Sensor aktiviert? (ja/nein): ").lower() == 'ja'
    
    def write_output(self):
        # Merker auslesen und auf Ausgänge setzen
        print(f"Motor: {'An' if self.outputs['motor'] else 'Aus'}")
        print(f"Alarm: {'An' if self.outputs['alarm'] else 'Aus'}")
        print(f"Aktueller Zustand: {self.state}")

    def cycle(self):
        self.read_input()
        self.logic()
        self.write_output()
        print("-" * 30)

    def logic(self):
        if self.state_now == 'RESET' and self.state_last == 'RESET':
            # First RUN after Start PLC
            print("PLC -> Einschaltwischer")
            self.state_now = 'DEFAULT'

def main():
    state = 'RUN'
    plc = PLC()
    print(plc.set_state(state))
    #plc.cycle()

# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################

if __name__ == "__main__":

    main()
