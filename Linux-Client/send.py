from PIL import Image 
import gtk.gdk
import httplib, urllib, threading

def get():
    w = gtk.gdk.get_default_root_window()
    # sz = [w.get_size()]
    # print "The size of the window is %d x %d" % sz
    
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,1920,1080)
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,1920,1080)
    
    height=pb.get_height()
    width=pb.get_width()
    i = Image.frombuffer("RGB", (width,height) ,pb.pixel_array, 'raw', 'RGB', 0, 1)
    h = i.histogram()
    i = None
    # split into red, green, blue
    r = h[0:256]
    g = h[256:256*2]
    b = h[256*2: 256*3]

    print sum( i*w for i, w in enumerate(r) ) / sum(r),
    print sum( i*w for i, w in enumerate(g) ) / sum(g),
    print sum( i*w for i, w in enumerate(b) ) / sum(b)
    params = urllib.urlencode({'red': sum(i*w for i, w in enumerate(r) ) / sum(r), 'green' : sum( i*w for i, w in enumerate(g) ) / sum(g), 'blue': sum( i*w for i, w in enumerate(b) ) / sum(b)})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection("raspberrypi.local:3000")
    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    conn.close()

while True :
    get()
