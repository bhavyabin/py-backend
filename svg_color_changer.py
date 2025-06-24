from svghelper import set_color
import glob

files = [
    "sunrise",
    "sunset",
    "moonrise",
    "moonset",
]

for filename in files:
    set_color(fr"D:\Bhavya\HTML Files\hello_angular\python_backend\static\wi-{filename}.svg",fr"D:\Bhavya\HTML Files\hello_angular\python_backend\static\wi-{filename}.svg","#000000")

print("done")