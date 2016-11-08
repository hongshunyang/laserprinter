#!/usr/bin/env python
# vim:set et ts=4 sw=4 tw=80:
# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.3 on Thu Jun 17 13:44:35 2010

import wx
import os,sys,gettext

sys.path.append("../wx")
sys.path.append("../lib")
sys.path.append("../module")

from LPFrame import LPFrame

class lpApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        self.LPFrame = LPFrame(None, -1, "")
        self.SetTopWindow(self.LPFrame)
        self.LPFrame.Show()
        return 1

# end of class lpApp


if __name__ == "__main__":

   gettext.install('app')
   laserPrinter = lpApp(0)
   laserPrinter.MainLoop()
   sys.exit()

