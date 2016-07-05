class station(object):
    def __init__ (self, name, tempX, tempY):
        self.name = name
        self.x = tempX
        self.y = tempY
        print (self.x, " ", self.y, " ", self.name)
    def display(self):
        fill(255)
        ellipse(self.x,self.y,10,10)
        
class passenger(object):
    def __init__ (self, tempX, tempY):
        self.x = tempX
        self.y = tempY
    def display(self):
        fill(100)
        ellipse(self.x,self.y,5,5)
    def findDestination(x,y):
        print "hi"
    
stations = []
passengers =[]
height = 500
width = 500    
    
    
    
def setup():
    size(height,width)
    createStations()
    passengers.append(passenger(50,50))
    
def draw():
    background(255)
    for i in range(len(stations)):
        stations[i].display()
    for i in range(len(passengers)):
        passengers[i].display()
        
    # Below is test of dist() function    
    for i in range(len(stations)):
        print(dist(50,50,stations[i].x,stations[i].y))
        
        
def createStations():
    stations.append(station("Oslo",150,150))
    stations.append(station("Bergen",250,350))
    stations.append(station("Trondheim",100,300))
    stations.append(station("Stavanger",450,200))
    print "Stations created ", len(stations)
    print stations
    
