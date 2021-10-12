#init i2c bus, first import the needed libraries (I2C and SSD1306 Driver), then instantiate I2C + Driver
import board
import busio as io
import adafruit_ssd1306

class On_Display:
    def __init__(self): #define the class constructor (master will usually be an instance of tk.Tk())
        #create an instance of the ssd1306 I2C driver
        self.oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
        #create i2c instance
        self.i2c = io.I2C(board.SCL, board.SDA)
        self.draw_labels() #make sure the labels are drawn
            
    def draw_labels(newTemp, conDevice):
        
        self.oled.fill(0) #clear screen and then write the text, more labels can be added if needed (not much though)
        self.oled.text('Temp: ', 0, 0)
        self.oled.text('Device: ', 0, 20)
        
        if newTemp is not None: #make sure newTemp actually exists before trying to write it
            self.oled.text(newTemp, 15, 0)
        else:
            self.oled.text('No Temp', 15, 0)    
                    
        if conDevice is not None: #make sure conDevice actually exists before trying to write it
            self.oled.text(conDevice, 15, 20)
        else:
            self.oled.text('No Device', 15, 20)   
                    
        self.oled.show() #show the text that was just drawn, nuff said