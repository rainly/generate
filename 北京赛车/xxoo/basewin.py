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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"北京赛车(数字盘)", pos = wx.DefaultPosition, size = wx.Size( 500,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"网址：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		bSizer3.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		self.m_url = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 340,-1 ), 0 )
		bSizer3.Add( self.m_url, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"进入", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"购买规则（位置,位置 换行）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_rules = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,100 ), wx.TE_MULTILINE|wx.TE_RICH2 )
		bSizer2.Add( self.m_rules, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"方案金额（序号=金额=赢序号=输序号 换行）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_monerys = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,100 ), wx.TE_MULTILINE|wx.TE_RICH2 )
		bSizer2.Add( self.m_monerys, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"购买道（道序号,道序号，...）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_buynos = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), wx.TE_MULTILINE|wx.TE_RICH2 )
		bSizer2.Add( self.m_buynos, 0, wx.ALL, 5 )
		
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
		self.m_button3.Bind( wx.EVT_BUTTON, self.onEnter )
		self.m_button1.Bind( wx.EVT_BUTTON, self.onsave )
		self.m_button2.Bind( wx.EVT_BUTTON, self.onstart )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onEnter( self, event ):
		event.Skip()
	
	def onsave( self, event ):
		event.Skip()
	
	def onstart( self, event ):
		event.Skip()
	

