import wx
import wx.animate     # ..\wx\animate.py
class MyPanel(wx.Panel):
    """ class MyPanel creates a panel, inherits wx.Panel """
    def __init__(self, parent, id):
        # default pos and size creates a panel that fills the frame
        wx.Panel.__init__(self, parent, id)
        self.SetBackgroundColour("white")
        # pick the filename of an animated GIF file you have ...
        # give it the full path and file name!
        ag_fname = "giphy.gif"
        ag = wx.animate.GIFAnimationCtrl(self, id, ag_fname, pos=(10, 10))
        # clears the background
        ag.GetPlayer().UseBackgroundColour(True)
        # continuously loop through the frames of the gif file (default)
        ag.Play()

def main1():
    app = wx.PySimpleApp()
    frame = wx.Frame(None, -1, "wx.animate.GIFAnimationCtrl()", size = (500, 400))
    # call the derived class, -1 is default ID
    MyPanel(frame, -1)
    frame.Show(True)
    app.MainLoop()



if __name__ == '__main__':
    main1()
