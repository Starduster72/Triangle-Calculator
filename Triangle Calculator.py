import math
import decimal
from decimal import Decimal

print('Triangle Calculator v1.0.0')

def standard_mode():
    print('Standard Mode')
    print('Set Unknown Value as X')

    n = 0

    a = False
    b = False
    c = False

    A = False
    B = False
    C = False

    global a_side
    global b_side
    global c_side

    global a_angle
    global b_angle
    global c_angle
    
    #Variable Inputs
    a_side = input('Side A: ')
    b_side = input('Side B: ')
    c_side = input('Side C: ')

    a_angle = input('Angle A: ')
    b_angle = input('Angle B: ')
    c_angle = input('Angle C: ')

    #Side Variables
    if a_side == 'X':
        a = False
    else:
        a_side = float(a_side)
        a = True

    if b_side == 'X':
        b = False
    else:
        b_side = float(b_side)
        b = True
    
    if c_side == 'X':
        c = False
    else:
        c_side = float(c_side)
        c = True
    
    #Angle Variables
    if a_angle == 'X':
        A = False
    else:
        a_angle = float(a_angle)
        a_angle = math.radians(a_angle)
        A = True

    if b_angle == 'X':
        B = False
    else:
        b_angle = float(b_angle)
        b_angle = math.radians(b_angle)
        B = True

    if c_angle == 'X':
        C = False
    else:
        c_angle = float(c_angle)
        c_angle = math.radians(c_angle)
        C = True
    
    def answers(a_side, b_side, c_side, a_angle, b_angle, c_angle):
        #Variable Checking
        a_angle = math.degrees(a_angle)
        a_angle = round(a_angle, 5)
        b_angle = math.degrees(b_angle)
        b_angle = round(b_angle, 5)
        c_angle = math.degrees(c_angle)
        c_angle = round(c_angle, 5)

        a_side = round(a_side, 5)
        b_side = round(b_side, 5)
        c_side = round(c_side, 5)

        n = 0

        if float(a_side) + float(b_side) < float(c_side):
            print(a_side, b_side, c_side)
            print('ERROR: Improper Variables 001')
            standard_mode()
        elif float(a_side) + float(c_side) < float(b_side):
            print('ERROR: Improper Variables 001')
            standard_mode()
        elif float(b_side) + float(c_side) < float(a_side):
            print('ERROR: Improper Variables 001')
            standard_mode()
        
        elif float(a_angle) + float(b_angle) + float(c_angle) > 181:
            if float(a_angle) + float(b_angle) + float(c_angle) < 179:
                print('ERROR: Improper Variables 002')
                standard_mode()

        else:
            print('Side A:', a_side)
            print('Side B:', b_side)
            print('Side C:', c_side)
            print('Angle A:', a_angle)
            print('Angle B:', b_angle)
            print('Angle C:', c_angle)
            standard_mode()

    def calculate(n, a, b, c, A, B, C, a_side, b_side, c_side, a_angle, b_angle, c_angle):
        #Math Handling
        if a and b and not c:
            if A and not B and not C:
                u = float(b_side) * math.sin(a_angle)
                u = u / float(a_side)
                b_angle = math.acos(u)
                B = True
            elif B and not A and not C:
                i = float(a_side) * math.sin(b_angle)
                i = i / float(b_side)
                a_angle = math.acos(i)
                A = True
            elif C and not A and not B:
                e = 2 * float(a_side) * float(b_side)
                y = float(b_side) **2
                x = float(a_side) **2
                o = y + x - e * math.cos(c_angle)
                c_side = math.sqrt(o)
                c = True
        
        if a and c and not b:
            if A and not B and not C:
                u = float(c_side) * math.sin(a_angle)
                u = u / float(a_side)
                c_angle = math.acos(u)
                C = True
            elif B and not A and not C:
                r = 2 * float(a_side) * float(c_side)
                x = float(a_side) **2
                z = float(c_side) **2
                i = x + z - r * math.cos(b_angle)
                b_side = math.sqrt(i)
                b = True
            elif C and not A and not B:
                o = float(a_side) * math.sin(c_angle)
                o = o / float(c_side)
                a_angle = math.acos(o)
                A = True
        
        if b and c and not a:
            if A and not B and not C:
                t = 2 * float(b_side) * float(c_side)
                y = float(b_side) **2
                z = float(c_side) **2
                u = y + z - t * math.cos(a_angle)
                a_side = math.sqrt(u)
                a = True
            elif B and not A and not C:
                i = float(c_side) * math.sin(b_angle)
                i = i / float(b_side)
                c_angle = math.acos(i)
                C = True
            elif C and not A and not B:
                o = float(b_side) * math.sin(c_angle)
                o = o / float(c_side)
                b_angle = math.asin(o)
                B = True

        if a and b and c:
            if not C:
                e = 2 * float(a_side) * float(b_side)
                x = float(a_side) **2
                y = float(b_side) **2
                z = float(c_side) **2
                u = x + y - z
                u = u / e
                c_angle = math.acos(u)
                C = True
            if not B:
                r = 2 * float(a_side) * float(c_side)
                x = float(a_side) **2
                y = float(b_side) **2
                z = float(c_side) **2
                i = z + x - y
                i = i / r
                b_angle = math.acos(i)
                B = True
            if not A:
                t = 2 * float(b_side) * float(c_side)
                x = float(a_side) **2
                y = float(b_side) **2
                z = float(c_side) **2
                o = y + z - x
                o = o / t
                a_angle = math.acos(o)
                A = True
        
        if A and B and not C:
            a_angle = math.degrees(a_angle)
            b_angle = math.degrees(b_angle)
            c_angle = 180 - a_angle - b_angle
            a_angle = math.radians(a_angle)
            b_angle = math.radians(b_angle)
            c_angle = math.radians(c_angle)
            C = True
        if A and C and not B:
            a_angle = math.degrees(a_angle)
            c_angle = math.degrees(c_angle)
            b_angle = 180 - a_angle - c_angle
            a_angle = math.radians(a_angle)
            b_angle = math.radians(b_angle)
            c_angle = math.radians(c_angle)
            B = True
        if B and C and not A:
            b_angle = math.degrees(b_angle)
            c_angle = math.degrees(c_angle)
            a_angle = 180 - c_angle - b_angle
            a_angle = math.radians(a_angle)
            b_angle = math.radians(b_angle)
            c_angle = math.radians(c_angle)
            A = True
        
        if A and B:
            if b and not a:
                u = float(b_side) * math.sin(a_angle)
                a_side = u / math.sin(b_angle)
                a_side = round(a_side, 5)
                a = True
            
            elif a and not b:
                i = float(a_side) * math.sin(b_angle)
                b_side = i / math.sin(a_angle)
                b_side = round(b_side, 5)
                b = True

        if A and C:
            if a and not c:
                o = float(a_side) * math.sin(c_angle)
                c_side = o / math.sin(a_angle)
                c_side = round(c_side, 5)
                c = True
            elif c and not a:
                u = float(c_side) * math.sin(a_angle)
                a_side = u / math.sin(c_angle)
                a_side = round(a_side, 5)
                a = True

        if B and C:
            if b and not c:
                i = float(b_side) * math.sin(c_angle)
                c_side = i / math.sin(b_angle)
                c_side = round(c_side, 5)
                c = True
            elif c and not b:
                i = float(c_side) * math.sin(b_angle)
                b_side = i / math.sin(c_angle)
                b_side = round(b_side, 5)
                b = True
                
        if A and B and C and a and b and c:
            answers(a_side, b_side, c_side, a_angle, b_angle, c_angle)
        
        elif n <= 0:
            n = 1
        
        else:
            print('ERROR: Invalid Variables 003')
            standard_mode()

    calculate(n, a, b, c, A, B, C, a_side, b_side, c_side, a_angle, b_angle, c_angle)

standard_mode()