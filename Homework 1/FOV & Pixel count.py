# Compute the Field of View of the camera

# Compute the Field of View of the camera in the Horizontal direction
import math

def horizontal_FOV(horizontal_sensor_size, focal_length):
    fov = 2*math.atan(horizontal_sensor_size/(2*focal_length))
    return(fov)

h = math.degrees(horizontal_FOV(14,25))
print(f"{h} degrees horizontal FOV")

# Compute the Field of View of the camera in the Vertical direction

def vertical_FOV(vertical_sensor_size, focal_length):
    fov = 2*math.atan(vertical_sensor_size/(2*focal_length))
    return(fov)

v = math.degrees(vertical_FOV(14,25))
print(f"{h} degrees vertical FOV")


# Compute the minimum number of pixels occupied by the object
# For this program the dimension of an object is in cm, focal lenght is in mm, distance is in meters

def numbers_of_pixels(height, width, focal_length, distance):
    distance_from_lens = (((distance*1000)*focal_length)/((distance*1000)-focal_length))
    height_pixel = (((height*10)*distance_from_lens)/(distance*1000))
    width_pixel = (((width*10)*distance_from_lens)/(distance*1000))
    area = (height_pixel*width_pixel)
    pixels_use = ((area*5000000)/196)
    return pixels_use

p = numbers_of_pixels(5, 5, 25, 20)
print(f"{p} pixels are used by the object")


# End of project 0