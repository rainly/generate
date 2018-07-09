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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"账号检测神器", pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"手机前缀：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		bSizer21.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		self.m_prefix = wx.TextCtrl( self, wx.ID_ANY, u"18150155", wx.DefaultPosition, wx.Size( 440,-1 ), wx.TE_MULTILINE )
		bSizer21.Add( self.m_prefix, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer21, 1, wx.EXPAND, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"转账金额：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer22.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_amount = wx.TextCtrl( self, wx.ID_ANY, u"0.01", wx.DefaultPosition, wx.Size( 440,-1 ), 0 )
		bSizer22.Add( self.m_amount, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer22, 1, wx.EXPAND, 5 )
		
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"显示名字：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		bSizer23.Add( self.m_staticText31, 0, wx.ALL, 5 )
		
		self.m_show_name = wx.TextCtrl( self, wx.ID_ANY, u"哈哈，看到没", wx.DefaultPosition, wx.Size( 440,-1 ), 0 )
		bSizer23.Add( self.m_show_name, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer23, 1, wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText311 = wx.StaticText( self, wx.ID_ANY, u"显示备注：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText311.Wrap( -1 )
		bSizer24.Add( self.m_staticText311, 0, wx.ALL, 5 )
		
		self.m_remark = wx.TextCtrl( self, wx.ID_ANY, u"哈哈", wx.DefaultPosition, wx.Size( 440,-1 ), 0 )
		bSizer24.Add( self.m_remark, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer24, 1, wx.EXPAND, 5 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3111 = wx.StaticText( self, wx.ID_ANY, u"启动线程：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3111.Wrap( -1 )
		bSizer25.Add( self.m_staticText3111, 0, wx.ALL, 5 )
		
		self.m_threadnum = wx.TextCtrl( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 440,-1 ), 0 )
		bSizer25.Add( self.m_threadnum, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer25, 1, wx.EXPAND, 5 )
		
		gSizer25 = wx.GridSizer( 1, 2, 200, 0 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"开始", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( gSizer25, 1, wx.EXPAND, 5 )
		
		
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
	

