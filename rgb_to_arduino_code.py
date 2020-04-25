import csv

data = []
pixelsX = 32  # change later to be variable
pixelsY = 32  # change later to be variable

with open('img_rgb_data.csv', 'r', newline='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        data.append(row)

for item in data:  # gets rid of last element. idk why it is processing as a 4 vector color.. look into later
    item.pop()

print(data)





# .......... format of arduino code ............... #
# void setup() {

#  matrix.begin();
#
#  // draw a pixel in solid white
#  matrix.drawPixel(0, 0, matrix.Color333(7, 7, 7));
# delay(500);
# .......... format of arduino code end............... #
