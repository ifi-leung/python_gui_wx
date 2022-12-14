import wx
import w_frame_xrc

class w_frame(w_frame_xrc.w_frame_xrc):
    def __init__(self, parent):
        super(w_frame, self).__init__(parent)

        self.m_listCtrl_info.ClearAll()
        self.m_listCtrl_info.InsertColumn(0, u'名字', width=140)

        self.m_button_add.Bind(wx.EVT_BUTTON, self.on_button_add)

    def on_button_add(self, event):
        value = self.m_textCtrl_name.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            self.m_listCtrl_info.InsertItem(self.m_listCtrl_info.GetItemCount(), value)
            self.m_textCtrl_name.Clear()