#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# vim:set et ts=4 sw=4 tw=80:

class lpMisc():
    # seconds to time string
    @staticmethod
    def sec2time(sec):
        sec=int(sec)	
        h=sec/3600
        sUp_h=sec-3600*h
        m=sUp_h/60
        sUp_m=sUp_h-60*m
        s=sUp_m
        text_hour=_("hour")
        text_minute=_("minute")
        text_sec=_("seconds")
        timestr="%s%s%s%s%s%s" %(h,text_hour,m,text_minute,s,text_sec)
        return timestr
