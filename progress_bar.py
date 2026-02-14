class ProgressBar:
  def __init__(self):
    self.graph = ["0        20        40        60        80       100",
                  "|----+----|----+----|----+----|----+----|----+----|"]
    
    self.track = "="
    self.render_gui()

  def render_gui(self):
    for row in self.graph:
      print(row)
        
    print(self.track, end='\r')