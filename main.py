# БАЗОВАЯ ВЕРСИЯ КОДА
# ДЛЯ ESP32 DEV MODULE
from machine import Pin, SoftI2C
import ssd1306
 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64  # 32 ДЛЯ ДИСПЛЕЯ 128X32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('First Row!', 0, 0)
oled.text('Second Row!', 0, 20)
oled.text('Third Row!', 0, 30)
oled.text('Fourth Row!', 0, 40)
oled.text('Fifth Row!', 0, 50)
        
oled.show()

# УЛУЧШЕННАЯ ВЕРСИЯ КОДА (ВМЕЩАЕТСЯ БОЛЬШЕ СТРОК)
# ДЛЯ ESP32-S3-DEV-KIT-N8R8
from machine import Pin, SoftI2C
import ssd1306

# Инициализация (твои пины)
i2c = SoftI2C(scl=Pin(47), sda=Pin(21))

W = 128
H = 64
oled = ssd1306.SSD1306_I2C(W, H, i2c)

def center_text(oled, text, y):
    x = (W - len(text)*8) // 2   # базовый расчёт для 8x8 шрифта
    if x < 0:
        x = 0
    oled.text(text, x, y)

oled.fill(0)

rows = ['1st Row!', '2nd Row!', '3rd Row!', '4th Row!',
        '5th Row!', '6th Row!', '7th Row!', '8th Row!']
# y-координаты кратны 8: 0,8,16,24,32,40  (вместится 8 строк максимум при 8px)
for i, r in enumerate(rows):
    y = i * 8
    center_text(oled, r, y)

oled.show()