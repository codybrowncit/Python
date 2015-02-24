import pygtk
import gtk

class SliderGUI:
  def __init__(self, size, imagefilename):
    self.pixbuf=[]
    self.images=[]
    self.buttons=[]
    self.size= size
    self.readImageFile(imagefilename)
    self.cell_width= self.full_width/self.size
    self.cell_height= self.full_height/self.size
    self.createWindow()
    self.createBtnImages()
    self.createMenu()
    self.createGame()
    self.win.show_all()
    self.logic=SliderLogic(self.size)
    self.updateDisplay()

  def readImageFile(self, imagefilename):
    image=gtk.Image()
    image.set_from_file(imagefilename)
    pixbuf=image.get_pixbuf()
    self.full_height= pixbuf.get_height()
    self.full_width= pixbuf.get_width()
    self.full_pixbuf=pixbuf
      
  def createWindow(self):
    self.win= gtk.Window(gtk.WINDOW_TOPLEVEL)
    self.win.set_title('Slider Game')
    self.win.set_resizable(False)
    self.win.connect('delete_event', self.delete_handler)
    self.win.connect('destroy', self.destroy_handler)
    self.win.set_default_size(self.full_width,self.full_height)
    self.main_vbox= gtk.VBox(False, 0)
    self.win.add(self.main_vbox)

  def createBtnImages(self):
    for yval in range (0, self.full_height, self.cell_height):
      for xval in range (0, self.full_width, self.cell_width):
        subpixbuf = self.full_pixbuf.subpixbuf(xval, yval,
                self.cell_width, self.cell_height)
        self.pixbuf.append(subpixbuf)
      
  def createMenuItem(self, title, handler):
    item=gtk.MenuItem(title)
    item.connect('activate', handler, None)
    self.menu.append(item)
    
  def createMenu(self):
    self.menu=gtk.Menu()
    self.createMenuItem('New Game', self.restart_handler)
    self.createMenuItem('Solve', self.solve_handler)
    self.createMenuItem('Quit', self.destroy_handler)
    self.root_menu=gtk.MenuItem('Game')
    self.root_menu.set_submenu(self.menu)
    self.menubar=gtk.MenuBar()
    self.menubar.add(self.root_menu)
    self.main_vbox.pack_start(self.menubar)
    
  def createGame(self):
    table=gtk.Table(self.size, self.size, True)
    for row in range(self.size):
      for col in range(self.size):
        button=gtk.Button()
        image=gtk.Image()
        index= row*self.size+col
        image.set_from_pixbuf(self.pixbuf[index])
        button.add(image)
        self.images.append(image)
        self.buttons.append(button)
        button.connect('clicked', self.clicked_handler, index)
        table.attach(button, col, col+1, row, row+1)
    self.main_vbox.pack_start(table)
        
  def delete_handler(self, widget, event, data=None):
    return False
  
  def destroy_handler(self, widget, data=None):
      self.win.destroy() 
      gtk.main_quit()
    
  def restart_handler(self, widget, data=None):
    print ('restart')
    self.logic.restart()
    self.logic.shuffle()
    self.updateDisplay()
    

  def solve_handler(self, widget, data=None):
    print ('solve')

  def clicked_handler(self, widget, data=None):
    print ('clicked', data)
    self.logic.takeTurn(self)
    
  def updateDisplay(self):
    hole=self.logic.getHole()
    for i in range(len(self.buttons)):
      self.logic.getCell(self)
      pxibuf= self.pixbuf[i]
      image= self.createGame()
      if image == hole:
        image.hide
    
    
    
  def run(self):
      gtk.main()

      
class SliderLogic:
  def __init__(self, size):
    self.size=size
    self.restart()
    self.shuffle(100)

  def restart(self):
    self.cells=[]
    for rows in range(self.size):
      for cols in range(self.size):
        self.cells.append(rows)
    self.hole= self.cells[-1]

  def legalNeighbors(self, n):
    neighbors=[]
    for i in range(self.size^6):
      if self.hole % self.size > 0:
        neighbors.append(self.hole - 1)
      elif self.hole % self.size < 3:
        neighbors.append(self.hole +1)
      elif self.hole >= self.size:
        neighbors.append(self.hole - self.size)
      elif self.hole >= -self.size-1:
        neighbors.append(self.hole + self.size)
        return neighbors
##      if self.hole -1 == i or
##        self.hole +1 == i or
##        self.hole -self.size == i or
##        self.hole +self.size == i:
##        row = i/self.size
##        cols = i/self.size

          
        

  def shuffle(self, count):
    for i in range(count):
      self.restart()

  def takeTurn(self, n):
    turn= self.getCell(n)
    if self.legalNeighbors(turn):
      self.swapCells(turn)
    
  def swapCells(self, n):
    location=n
    

  def getCell(self, n):
    return self.cells[n]

  def getHole(self):
    return self.hole
  
def main():
  s=SliderGUI(4, 'smiley.gif')
  s.run()
main()
