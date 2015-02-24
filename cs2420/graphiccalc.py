from graphics import *


class my_stack:
    
    def __init__(self):
        self.mystack = []
        self.mystack2 = []
        
    def pop(self):
        return self.mystack.pop()
        
    def push(self, a):
        self.mystack.append(a)
    
    def isEmpty(self):
        if len(self.mystack) == 0:
            return True
        return False
        
    def top(self):
        return self.mystack[-1]


def InfixToPostfix(infix):
    postfix = " "
    opstack = my_stack()
    for c in infix:
        print c
        if c.isdigit() or c == 'x' or c == 'X':
            postfix += c
        elif c == '(':
            opstack.push(c)
        elif c == ')':
            while opstack.top() !='(':
                postfix += opstack.pop()
            opstack.pop()
        elif c in ['+', '-']:
            while not opstack.isEmpty() and  opstack.top() in ['+', '-', '*', '/']:   
                postfix += opstack.pop()
            opstack.push(c)
        elif c in ['*', '/']:
            while not opstack.isEmpty() and  opstack.top() in ['*', '/']:   
                postfix += opstack.pop()
            opstack.push(c)
    while not opstack.isEmpty():
        postfix += opstack.pop()

    return postfix

def EvaluatePostfix(x, postfix):
    opstack = my_stack()
    for c in postfix:
        if c.isdigit():
            opstack.push(float(c))
        elif c in ['x', 'X']:
            opstack.push(x)
        elif opstack.isEmpty() == False:
            right = float(opstack.pop())
            if opstack.isEmpty():
                return v
            left = float(opstack.pop())
            if c == '+':
                v = left + right
            if c == '-':
                v = left - right
            if c == '*':
                v =  left * right
            if c == '/':
                v = left / right
            opstack.push(v)
    return opstack.pop()
    
    
def print_instructions():
    print "This graphing calculator can graph basic formulas to a graph, from your input"

def main():
    print_instructions()
    infix = raw_input("Enter your formula: Example 'x*x/(x+3)' ")
    postfix = InfixToPostfix(infix)
    win = GraphWin("Graphing Calculator", 600, 700)

    left = -10
    bottom = -10
    top = 10
    right = 10

    line = Line(Point(0, 35), Point(700, 35))
    line.setWidth(1)
    line.setOutline("gray")
    line.draw(win)
    label=Text(Point(306, 66), '8')
    label.draw(win)
    line = Line(Point(0, 70), Point(700, 70))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    line = Line(Point(0, 105), Point(700, 105))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(306, 136), '6')
    label.draw(win)
    line = Line(Point(0, 140), Point(700, 140))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    line = Line(Point(0, 175), Point(700, 175))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(306, 206), '4')
    label.draw(win)
    line = Line(Point(0, 210), Point(700, 210))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    line = Line(Point(0, 245), Point(700, 245))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(306, 276), '2')
    label.draw(win)
    line = Line(Point(0, 280), Point(700, 280))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    line = Line(Point(0, 315), Point(700, 315))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    line = Line(Point(0, 350), Point(700, 350)) #center horizontal line
    line.setWidth(3)
    line.draw(win)
    line = Line(Point(0, 385), Point(700, 385))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(310, 416), '-2')
    label.draw(win)
    line = Line(Point(0, 420), Point(700, 420))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    line = Line(Point(0, 455), Point(700, 455))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(310, 486), '-4')
    label.draw(win)
    line = Line(Point(0, 490), Point(700, 490))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    line = Line(Point(0, 525), Point(700, 525))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(310, 556), '-6')
    label.draw(win)
    line = Line(Point(0, 560), Point(700, 560))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    line = Line(Point(0, 595), Point(700, 595))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(310, 626), '-8')
    label.draw(win)
    line = Line(Point(0, 630), Point(700, 630))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    line = Line(Point(0, 665), Point(700, 665))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    line = Line(Point(300, 0), Point(300, 700)) #Center vertical line
    line.setWidth(3)
    line.draw(win)
    label=Text(Point(328, 360), '1')
    label.draw(win)
    line = Line(Point(330, 0), Point(330, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(357, 360), '2')
    label.draw(win)
    line = Line(Point(360, 0), Point(360, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(387, 360), '3')
    label.draw(win)
    line = Line(Point(390, 0), Point(390, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(417, 360), '4')
    label.draw(win)
    line = Line(Point(420, 0), Point(420, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(447, 360), '5')
    label.draw(win)
    line = Line(Point(450, 0), Point(450, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(477, 360), '6')
    label.draw(win)
    line = Line(Point(480, 0), Point(480, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(507, 360), '7')
    label.draw(win)
    line = Line(Point(510, 0), Point(510, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(537, 360), '8')
    label.draw(win)
    line = Line(Point(540, 0), Point(540, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(567, 360), '9')
    label.draw(win)
    line = Line(Point(570, 0), Point(570, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win) # end of right side lines
    label=Text(Point(266, 360), '-1')
    label.draw(win)
    line = Line(Point(270, 0), Point(270, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(236, 360), '-2')
    label.draw(win)
    line = Line(Point(240, 0), Point(240, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(206, 360), '-3')
    label.draw(win)
    line = Line(Point(210, 0), Point(210, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(176, 360), '-4')
    label.draw(win)
    line = Line(Point(180, 0), Point(180, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(146, 360), '-5')
    label.draw(win)
    line = Line(Point(150, 0), Point(150, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(116, 360), '-6')
    label.draw(win)
    line = Line(Point(120, 0), Point(120, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(86, 360), '-7')
    label.draw(win)
    line = Line(Point(90, 0), Point(90, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(56, 360), '-8')
    label.draw(win)
    line = Line(Point(60, 0), Point(60, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    label=Text(Point(26, 360), '-9')
    label.draw(win)
    line = Line(Point(30, 0), Point(30, 700))
    line.setWidth(1)
    line.setOutline("grey")
    line.draw(win)
    
    win.setCoords(left, bottom, top, right)

    x = left
    xaxisInc = .1
    while x <= right:
        point1 = Point(x, EvaluatePostfix(x, postfix))
        point2 = Point(x + xaxisInc, EvaluatePostfix(x + xaxisInc, postfix))
        line = Line(point1, point2)
        line.setWidth(3)
        line.setOutline("blue")
        line.draw(win)
        x += xaxisInc

    p = win.getMouse()
    win.close()


main()
        
