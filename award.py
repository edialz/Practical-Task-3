# Constants for time thresholds
PROVINCIAL_COLOURS_MAX_TIME = 100
PROVISIONAL_HALF_COLOURS_MAX_TIME = 105
PROVINCIAL_SCROLL_MAX_TIME = 110

swimming_time = int(input("Enter swimming time: "))
cycling_time = int(input("Enter cycling time: "))
running_time = int(input("Enter running time: "))
shotput_time = int(input("Enter shot put time: "))  # New shot put time input

# Assuming the shot put time should be added to the total time
total_time = swimming_time + cycling_time + running_time + shotput_time

if total_time <= PROVINCIAL_COLOURS_MAX_TIME:
    print("Provincial Colours")
elif total_time <= PROVISIONAL_HALF_COLOURS_MAX_TIME:
    print("Provisional Half Colours")
elif total_time <= PROVINCIAL_SCROLL_MAX_TIME:
    print("Provincial Scroll")
else:
    print("No award")

