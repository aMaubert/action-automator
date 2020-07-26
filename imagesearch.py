import os
from time import perf_counter

from python_imagesearch.imagesearch import imagesearch, imagesearcharea, region_grabber, click_image

def imagesearch_example():
    for file in os.listdir(os.path.curdir):
        if file.lower().endswith('.png'):
            pos = imagesearch(file)
            if type(pos) is tuple:
                print("position : ", pos[0], pos[1])
            else:
                print("image not found")

def imagesearcharea_example():
    for file in os.listdir(os.path.curdir):
        if file.lower().endswith('.png'):
            pos = imagesearcharea(file, x1=0, y1=0, x2=490, y2=800)
            if type(pos) is tuple:
                print("position : ", pos[0], pos[1])
            else:
                print("image not found")

# Very useful to optimize imagesearcharea or imagesearch calls,
# by getting an already processed image you can perform multiple searches on it with great speed gains
def region_grabber_example():
    image_region = region_grabber(region=(0, 0, 800, 600))
    for file in os.listdir(os.path.curdir):
        if file.lower().endswith('.png'):
            pos = imagesearcharea(file, x1=0, y1=0, x2=800, y2=600, precision=0.8, im=image_region)
            if type(pos) is tuple:
                print("position : ", pos[0], pos[1])
            else:
                print("image not found")

def click_image_example():
    image_region = region_grabber(region=(0, 0, 800, 600))
    for file in os.listdir(os.path.curdir):
        if file.lower().endswith('.png'):
            pos = imagesearcharea(file, x1=0, y1=0, x2=800, y2=600, precision=0.8, im=image_region)
            if type(pos) is tuple:
                print("position : ", pos[0], pos[1])
                click_image(image=file, pos=pos, action="left", timestamp=0)
            else:
                print("image not found")

if __name__ == '__main__':
    time1 = perf_counter()
    print("======= imagesearch_example =======")
    imagesearch_example()
    print(str(perf_counter() - time1))
    print("======= imagesearcharea_example =======")
    imagesearcharea_example()
    print(str(perf_counter() - time1))
    print("======= region_grabber_example =======")
    region_grabber_example()
    print(str(perf_counter() - time1))

    click_image_example()