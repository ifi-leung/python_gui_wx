import wx
import w_frame

app = wx.App()
window = w_frame.w_frame(parent=None)
window.Show()
app.MainLoop()