
class MapHexagone():
  
  width: int
  height: int
  
  def __init__(self, width, height):
    self.width = width
    self.height = height
    
  def __str__(self):
    ret = ""
    #adapt_height = self.height//2 + self.height%2
   # adapt_width = self.width//2 + self.width%2
    
    adapt_height = self.height
    adapt_width = self.width

    for j in range (adapt_width):
      ret += "  __    "
    ret += "\n"
    for i in range (adapt_height):
      for i in range (adapt_width):
        ret += " /  \\   "
      ret += "\n"
      for i in range (adapt_width):
        ret += "/    \\"
        if i != adapt_width-1:
          ret += "__"
      ret += "\n"
      for i in range (adapt_width):
        ret += "\\    /  "
      ret += "\n"
      for i in range (adapt_width):
        ret += " \\__/   "
      ret += "\n"
    return ret
    
    
    
    