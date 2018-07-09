# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class BaseMainWind
###########################################################################

class BaseMainWind ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"支付宝(转账工具)", pos = wx.DefaultPosition, size = wx.Size( 500,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"金额：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText41.Wrap( -1 )
        bSizer3.Add( self.m_staticText41, 0, wx.ALL, 5 )
        
        self.m_monery = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 440,-1 ), 0 )
        bSizer3.Add( self.m_monery, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"账号数据", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.m_users = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,300 ), wx.TE_MULTILINE|wx.TE_RICH2 )
        bSizer2.Add( self.m_users, 0, wx.ALL, 5 )
        
        gSizer2 = wx.GridSizer( 1, 2, 200, 0 )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.m_button1, 0, wx.ALL, 5 )
        
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"开始", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.m_button2, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( gSizer2, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer2 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.onsave )
        self.m_button2.Bind( wx.EVT_BUTTON, self.onstart )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def onsave( self, event ):
        event.Skip()
    
    def onstart( self, event ):
        event.Skip()
    

