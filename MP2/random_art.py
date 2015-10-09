# -*- coding: utf-8 -*-
"""
Random_art.py

@author: Jake
"""

# you do not have to use these particular modules, but they may help
from random import randint
from PIL import Image
import math

""" 
Using 3 functions to make random computer art
"""


def build_random_function(min_depth, max_depth):
    """ 
    building random functions using "prod","cos_pi","sin_pi" in depth of between min_depth and max_depth
    input: depth range(mindepth, maxdepth)
    output: random function(list)
    """

    
    pick_random_function=[["prod",'a','b'],["sin_pi",'a'],["cos_pi",'b']] #nested list of using functions
    pick_random_input=[['x'],['y']]   #nested list of depth 1 ( x, y)
    
    #using recursion put the function in the list
    #lowering the both arguments of the buid_random_function until the min_depth becomes 0
    if min_depth>1 and max_depth>=min_depth:
        randint_random_function=randint(0, 2) #get random number of(0,2) to pick random function
        random_function=pick_random_function[randint_random_function] #get random function from the function list
        
       
        if randint_random_function ==0: #if the function is 'prod' it needs two operands
            random_function[1]= build_random_function(min_depth-1, max_depth-1) #using recursion, put the build_random_function as a operand
            random_function[2]= build_random_function(min_depth-1, max_depth-1)
            
        else: #if the function is 'sin_pi' or 'cos_pi' it only needs one operand
            random_function[1]= build_random_function(min_depth-1, max_depth-1)
        return random_function
    
    # if the min_depth is 1 and maxdepth is larger than that the depth of the random function is already
    # same or larger than the min_depth. Therefore the max_depth argument in the build_random_function can be
    # any integer between 1 and max_depth-1
    elif min_depth==1 and max_depth>=2:
        randint_random_function=randint(0, 2)
        random_function=pick_random_function[randint_random_function]

        if randint_random_function==0: #if the functions is 'prod' it needs two operands
            random_function[1]= build_random_function(1, randint(1,max_depth-1)) #maximum depth: random value among 0~maxdepth-1
            random_function[2]= build_random_function(1, randint(1,max_depth-1))
             
        else: #if the function is 'sin_pi' or 'cos_pi'
            random_function[1]= build_random_function(1, randint(1,max_depth-1))
        return random_function

    # if the min_depth and the max_depth are all 1, the list should be x or y
    elif min_depth==1 and max_depth==1:
        random_function=pick_random_input[randint(0,1)] #get x or y randomly
        return random_function
                 


def evaluate_random_function(f, x, y): 
    """ 
    get the value of the random_function
    input: random_function, x value, y value
    output: result of the evaluation(float)
    """

    # if length of the random function is 1, it means the depth is 1
    # other than that it means the depth is larger than 1
    if len(f)>1:
        if f[0]== 'prod': #if the list is 'prod', evaluate product
            result=evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
            return result

       
        elif f[0]=='sin_pi': #if the list is 'sin_pi' calculate sine
            result=math.sin(math.pi*evaluate_random_function(f[1],x,y))
            
            return result
        elif f[0]=='cos_pi': #if the list is 'sin_pi' calculate cosine
            result=math.cos(math.pi*evaluate_random_function(f[1],x,y))
            
            return result
    elif len(f)==1: #in the depth of 1, put the x value and y value
        if f==['x']:
            result=x
            return result
        elif f==['y']:
            result=y
            return result



def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
    """
    # using linear equation remap the value
    # calculating slope, intercept 
    slope=(output_interval_end-output_interval_start)/(input_interval_end-input_interval_start)
    intercept=output_interval_start-slope*input_interval_start
    remap_val=slope*val+intercept
    return remap_val
    


pixel_x=800
pixel_y=450
im=Image.new("RGB",(pixel_x, pixel_y)) #making image with designated number of pixels

#rgb color random function
red_random_function=build_random_function(3,4) 
green_random_function=build_random_function(3,6)
blue_random_function=build_random_function(4,5)

##get the rgb value of every pixels
for x in range(pixel_x):
    for y in range(pixel_y):
        remap_x=remap_interval(x,0, pixel_x-1,-1.0,1.0) #remap each pixel to (-1,1)
        remap_y=remap_interval(y,0, pixel_y-1,-1.0,1.0)
        red_unremap=evaluate_random_function(red_random_function, remap_x, remap_y)#get the value of red random function
        red=remap_interval(red_unremap, -1.0, 1.0, 0, 255)#remap the red value to (0,255)

        green_unremap=evaluate_random_function(green_random_function, remap_x, remap_y)
        green=remap_interval(green_unremap, -1.0, 1.0, 0, 255)

        blue_unremap=evaluate_random_function(blue_random_function, remap_x, remap_y)
        blue=remap_interval(blue_unremap, -1.0, 1.0, 0, 255)
        new_color=(int(red),int(green),int(blue))#make tuple of RGB
        im.putpixel((x,y),new_color)
        
im.save('example2.png') 




