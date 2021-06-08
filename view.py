import eel
import desktop
import pos-system

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def pos-system(word,csvfile):
    pos-system(word,csvfile)
    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)