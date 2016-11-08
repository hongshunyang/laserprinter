#!/usr/bin/env python
# vim:set et ts=4 sw=4 tw=80:
# -*- coding: iso-8859-15 -*-

import wx

class LPGlobalData():
    def __init__(self):

        self.cfg = wx.Config('laserPrinterConf')
        self.StepLength=self.cfg.Read("StepLength","0.1")
        
        self.Vmanual=self.cfg.Read("Vmanual","200")
        self.Vscaning=self.cfg.Read("Vscaning","0.3")
        self.ComPort=self.cfg.ReadInt("ComPort",2)
        self.ComPort_string=self.cfg.Read("ComPortString","")
        self.Language=self.cfg.ReadInt("Language",1)
        self.LicenseRegistered=self.cfg.ReadInt("RUSR",0)
        self.WhetherMirrorX=self.cfg.ReadInt("MirrorX",0)
        
    def SaveCfg(self):
        self.cfg.Write("StepLength",self.StepLength)
        self.cfg.Write("Vmanual",self.Vmanual)
        self.cfg.Write("Vscaning",self.Vscaning)
        self.cfg.WriteInt("ComPort",self.ComPort)
        self.cfg.Write("ComPortString",self.ComPort_string)
        self.cfg.WriteInt("Language",self.Language)
        self.cfg.WriteInt("RUSR",self.LicenseRegistered)
        self.cfg.WriteInt("MirrorX",self.WhetherMirrorX)

