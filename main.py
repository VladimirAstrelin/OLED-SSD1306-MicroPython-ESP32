from machine import Pin, SoftI2C
import ssd1306
 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('First Row!', 0, 0)
oled.text('Second Row!', 0, 20)
oled.text('Third Row!', 0, 30)
oled.text('Fourth Row!', 0, 40)
oled.text('Fifth Row!', 0, 50)
        
oled.show()

# для 0,91-inch дисплея:
#from machine import Pin, SoftI2C
#import ssd1306
#i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
# oled_width = 128
#oled_height = 32
#oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
#oled.fill(0)  # Очистка дисплея
#oled.text('First Row!', 0, 0)
#oled.text('Second Row!', 0, 10)
#oled.text('Third Row!', 0, 20)
#oled.show()
