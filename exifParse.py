#Ruslan Karimov - Forensics Labs
from exif import Image
import sys
if __name__=="__main__":
    try:
        arg = sys.argv[1]
        with open(arg, 'rb') as image_file:
            image_file = Image(image_file)
        images = [image_file]
        for index, image in enumerate(images):
            print("Source File: " + arg)
            print(f"Make: {image.make}")
            print(f"Model: {image.model}")
            print(f"Original Date/Time: {image.datetime_original}")
            def coordinate_location_spacing(GPScoordinates):
                return f"{round(GPScoordinates[0])} degrees, {GPScoordinates[1]} minutes, {GPScoordinates[2]} seconds"
            direction = image.gps_longitude_ref
            if direction == "S" or direction == "W":
                DirectionSign = '-'
            else: 
                DirectionSign = ''
            print(f"Latitude: {coordinate_location_spacing(image.gps_latitude)} ")
            print(f"Longitude: {str(DirectionSign)+coordinate_location_spacing(image.gps_longitude)} ")
    except IndexError:
        print("Error! - No Image File Specified!")
    except IOError:
        print ("Error! - File Not Found!")
    except FileNotFoundError:
        print("Error! - File Not Found!")
        raise (SystemExit) 



            

            





    
    

