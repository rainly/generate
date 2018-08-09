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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"北京赛车", pos = wx.DefaultPosition, size = wx.Size( 500,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"网址：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText41.Wrap( -1 )
        bSizer1.Add( self.m_staticText41, 0, wx.ALL, 5 )
        
        self.m_url = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 340,-1 ), 0 )
        bSizer1.Add( self.m_url, 0, wx.ALL, 5 )
        
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"进入", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_button3, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer1, 1, wx.EXPAND, 5 )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"序号", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer3.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"玩法", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer3.Add( self.m_staticText6, 0, wx.ALL, 5 )
        
        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"起始金额", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"赢加减金额(+/-)", wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
        self.m_staticText8.Wrap( -1 )
        bSizer3.Add( self.m_staticText8, 0, wx.ALL, 5 )
        
        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"输加减金额(+/-)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer3.Add( self.m_staticText9, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
        
        bSizer40 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText410 = wx.StaticText( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        self.m_staticText410.Wrap( -1 )
        bSizer40.Add( self.m_staticText410, 0, wx.ALL, 5 )
        
        m_comboBox420Choices = [ u"大", u"小", u"单", u"双", u"龙", u"虎" ]
        self.m_comboBox420 = wx.ComboBox( self, wx.ID_ANY, u"大", wx.DefaultPosition, wx.Size( 80,-1 ), m_comboBox420Choices, 0 )
        bSizer40.Add( self.m_comboBox420, 0, wx.ALL, 5 )
        
        self.m_textCtrl430 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer40.Add( self.m_textCtrl430, 0, wx.ALL, 5 )
        
        self.m_textCtrl440 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer40.Add( self.m_textCtrl440, 0, wx.ALL, 5 )
        
        self.m_textCtrl450 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer40.Add( self.m_textCtrl450, 0, wx.ALL, 5 )
        
        self.m_checkBox460 = wx.CheckBox( self, wx.ID_ANY, u"启用", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer40.Add( self.m_checkBox460, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer40, 1, wx.EXPAND, 5 )
        
        bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText411 = wx.StaticText( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        self.m_staticText411.Wrap( -1 )
        bSizer41.Add( self.m_staticText411, 0, wx.ALL, 5 )
        
        m_comboBox421Choices = [ u"大", u"小", u"单", u"双", u"龙", u"虎" ]
        self.m_comboBox421 = wx.ComboBox( self, wx.ID_ANY, u"大", wx.DefaultPosition, wx.Size( 80,-1 ), m_comboBox421Choices, 0 )
        bSizer41.Add( self.m_comboBox421, 0, wx.ALL, 5 )
        
        self.m_textCtrl431 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer41.Add( self.m_textCtrl431, 0, wx.ALL, 5 )
        
        self.m_textCtrl441 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer41.Add( self.m_textCtrl441, 0, wx.ALL, 5 )
        
        self.m_textCtrl451 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer41.Add( self.m_textCtrl451, 0, wx.ALL, 5 )
        
        self.m_checkBox461 = wx.CheckBox( self, wx.ID_ANY, u"启用", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer41.Add( self.m_checkBox461, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer41, 1, wx.EXPAND, 5 )
        
        bSizer42 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText412 = wx.StaticText( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        self.m_staticText412.Wrap( -1 )
        bSizer42.Add( self.m_staticText412, 0, wx.ALL, 5 )
        
        m_comboBox422Choices = [ u"大", u"小", u"单", u"双", u"龙", u"虎" ]
        self.m_comboBox422 = wx.ComboBox( self, wx.ID_ANY, u"大", wx.DefaultPosition, wx.Size( 80,-1 ), m_comboBox422Choices, 0 )
        bSizer42.Add( self.m_comboBox422, 0, wx.ALL, 5 )
        
        self.m_textCtrl432 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer42.Add( self.m_textCtrl432, 0, wx.ALL, 5 )
        
        self.m_textCtrl442 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer42.Add( self.m_textCtrl442, 0, wx.ALL, 5 )
        
        self.m_textCtrl452 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer42.Add( self.m_textCtrl452, 0, wx.ALL, 5 )
        
        self.m_checkBox462 = wx.CheckBox( self, wx.ID_ANY, u"启用", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer42.Add( self.m_checkBox462, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer42, 1, wx.EXPAND, 5 )
        
        bSizer43 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText413 = wx.StaticText( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        self.m_staticText413.Wrap( -1 )
        bSizer43.Add( self.m_staticText413, 0, wx.ALL, 5 )
        
        m_comboBox423Choices = [ u"大", u"小", u"单", u"双", u"龙", u"虎" ]
        self.m_comboBox423 = wx.ComboBox( self, wx.ID_ANY, u"大", wx.DefaultPosition, wx.Size( 80,-1 ), m_comboBox423Choices, 0 )
        bSizer43.Add( self.m_comboBox423, 0, wx.ALL, 5 )
        
        self.m_textCtrl433 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer43.Add( self.m_textCtrl433, 0, wx.ALL, 5 )
        
        self.m_textCtrl443 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer43.Add( self.m_textCtrl443, 0, wx.ALL, 5 )
        
        self.m_textCtrl453 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer43.Add( self.m_textCtrl453, 0, wx.ALL, 5 )
        
        self.m_checkBox463 = wx.CheckBox( self, wx.ID_ANY, u"启用", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer43.Add( self.m_checkBox463, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer43, 1, wx.EXPAND, 5 )
        
        bSizer44 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText414 = wx.StaticText( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        self.m_staticText414.Wrap( -1 )
        bSizer44.Add( self.m_staticText414, 0, wx.ALL, 5 )
        
        m_comboBox424Choices = [ u"大", u"小", u"单", u"双", u"龙", u"虎" ]
        self.m_comboBox424 = wx.ComboBox( self, wx.ID_ANY, u"大", wx.DefaultPosition, wx.Size( 80,-1 ), m_comboBox424Choices, 0 )
        bSizer44.Add( self.m_comboBox424, 0, wx.ALL, 5 )
        
        self.m_textCtrl434 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer44.Add( self.m_textCtrl434, 0, wx.ALL, 5 )
        
        self.m_textCtrl444 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer44.Add( self.m_textCtrl444, 0, wx.ALL, 5 )
        
        self.m_textCtrl454 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer44.Add( self.m_textCtrl454, 0, wx.ALL, 5 )
        
        self.m_checkBox464 = wx.CheckBox( self, wx.ID_ANY, u"启用", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer44.Add( self.m_checkBox464, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer44, 1, wx.EXPAND, 5 )
        
        bSizer45 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText415 = wx.StaticText( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        self.m_staticText415.Wrap( -1 )
        bSizer45.Add( self.m_staticText415, 0, wx.ALL, 5 )
        
        m_comboBox425Choices = [ u"大", u"小", u"单", u"双" ]
        self.m_comboBox425 = wx.ComboBox( self, wx.ID_ANY, u"大", wx.DefaultPosition, wx.Size( 80,-1 ), m_comboBox425Choices, 0 )
        bSizer45.Add( self.m_comboBox425, 0, wx.ALL, 5 )
        
        self.m_textCtrl435 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer45.Add( self.m_textCtrl435, 0, wx.ALL, 5 )
        
        self.m_textCtrl445 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer45.Add( self.m_textCtrl445, 0, wx.ALL, 5 )
        
        self.m_textCtrl455 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer45.Add( self.m_textCtrl455, 0, wx.ALL, 5 )
        
        self.m_checkBox465 = wx.CheckBox( self, wx.ID_ANY, u"启用", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer45.Add( self.m_checkBox465, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer45, 1, wx.EXPAND, 5 )
        
        bSizer46 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText416 = wx.StaticText( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        self.m_staticText416.Wrap( -1 )
        bSizer46.Add( self.m_staticText416, 0, wx.ALL, 5 )
        
        m_comboBox426Choices = [ u"大", u"小", u"单", u"双" ]
        self.m_comboBox426 = wx.ComboBox( self, wx.ID_ANY, u"大", wx.DefaultPosition, wx.Size( 80,-1 ), m_comboBox426Choices, 0 )
        bSizer46.Add( self.m_comboBox426, 0, wx.ALL, 5 )
        
        self.m_textCtrl436 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer46.Add( self.m_textCtrl436, 0, wx.ALL, 5 )
        
        self.m_textCtrl446 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer46.Add( self.m_textCtrl446, 0, wx.ALL, 5 )
        
        self.m_textCtrl456 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer46.Add( self.m_textCtrl456, 0, wx.ALL, 5 )
        
        self.m_checkBox466 = wx.CheckBox( self, wx.ID_ANY, u"启用", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer46.Add( self.m_checkBox466, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer46, 1, wx.EXPAND, 5 )
        
        bSizer47 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText417 = wx.StaticText( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        self.m_staticText417.Wrap( -1 )
        bSizer47.Add( self.m_staticText417, 0, wx.ALL, 5 )
        
        m_comboBox427Choices = [ u"大", u"小", u"单", u"双" ]
        self.m_comboBox427 = wx.ComboBox( self, wx.ID_ANY, u"大", wx.DefaultPosition, wx.Size( 80,-1 ), m_comboBox427Choices, 0 )
        bSizer47.Add( self.m_comboBox427, 0, wx.ALL, 5 )
        
        self.m_textCtrl437 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer47.Add( self.m_textCtrl437, 0, wx.ALL, 5 )
        
        self.m_textCtrl447 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer47.Add( self.m_textCtrl447, 0, wx.ALL, 5 )
        
        self.m_textCtrl457 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer47.Add( self.m_textCtrl457, 0, wx.ALL, 5 )
        
        self.m_checkBox467 = wx.CheckBox( self, wx.ID_ANY, u"启用", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer47.Add( self.m_checkBox467, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer47, 1, wx.EXPAND, 5 )
        
        bSizer48 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText418 = wx.StaticText( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        self.m_staticText418.Wrap( -1 )
        bSizer48.Add( self.m_staticText418, 0, wx.ALL, 5 )
        
        m_comboBox428Choices = [ u"大", u"小", u"单", u"双" ]
        self.m_comboBox428 = wx.ComboBox( self, wx.ID_ANY, u"大", wx.DefaultPosition, wx.Size( 80,-1 ), m_comboBox428Choices, 0 )
        bSizer48.Add( self.m_comboBox428, 0, wx.ALL, 5 )
        
        self.m_textCtrl438 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer48.Add( self.m_textCtrl438, 0, wx.ALL, 5 )
        
        self.m_textCtrl448 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer48.Add( self.m_textCtrl448, 0, wx.ALL, 5 )
        
        self.m_textCtrl458 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer48.Add( self.m_textCtrl458, 0, wx.ALL, 5 )
        
        self.m_checkBox468 = wx.CheckBox( self, wx.ID_ANY, u"启用", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer48.Add( self.m_checkBox468, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer48, 1, wx.EXPAND, 5 )
        
        bSizer49 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText419 = wx.StaticText( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        self.m_staticText419.Wrap( -1 )
        bSizer49.Add( self.m_staticText419, 0, wx.ALL, 5 )
        
        m_comboBox429Choices = [ u"大", u"小", u"单", u"双" ]
        self.m_comboBox429 = wx.ComboBox( self, wx.ID_ANY, u"大", wx.DefaultPosition, wx.Size( 80,-1 ), m_comboBox429Choices, 0 )
        bSizer49.Add( self.m_comboBox429, 0, wx.ALL, 5 )
        
        self.m_textCtrl439 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer49.Add( self.m_textCtrl439, 0, wx.ALL, 5 )
        
        self.m_textCtrl449 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer49.Add( self.m_textCtrl449, 0, wx.ALL, 5 )
        
        self.m_textCtrl459 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer49.Add( self.m_textCtrl459, 0, wx.ALL, 5 )
        
        self.m_checkBox469 = wx.CheckBox( self, wx.ID_ANY, u"启用", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer49.Add( self.m_checkBox469, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer49, 1, wx.EXPAND, 5 )
        
        bSizer410 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4110 = wx.StaticText( self, wx.ID_ANY, u"11", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        self.m_staticText4110.Wrap( -1 )
        bSizer410.Add( self.m_staticText4110, 0, wx.ALL, 5 )
        
        m_comboBox4210Choices = [ u"合数大", u"合数小", u"合数单", u"合数双", wx.EmptyString ]
        self.m_comboBox4210 = wx.ComboBox( self, wx.ID_ANY, u"合数大", wx.DefaultPosition, wx.Size( 80,-1 ), m_comboBox4210Choices, 0 )
        bSizer410.Add( self.m_comboBox4210, 0, wx.ALL, 5 )
        
        self.m_textCtrl4310 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer410.Add( self.m_textCtrl4310, 0, wx.ALL, 5 )
        
        self.m_textCtrl4410 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer410.Add( self.m_textCtrl4410, 0, wx.ALL, 5 )
        
        self.m_textCtrl4510 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer410.Add( self.m_textCtrl4510, 0, wx.ALL, 5 )
        
        self.m_checkBox4610 = wx.CheckBox( self, wx.ID_ANY, u"启用", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer410.Add( self.m_checkBox4610, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer410, 1, wx.EXPAND, 5 )
        
        bSizer411 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4111 = wx.StaticText( self, wx.ID_ANY, u"12", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        self.m_staticText4111.Wrap( -1 )
        bSizer411.Add( self.m_staticText4111, 0, wx.ALL, 5 )
        
        m_comboBox4211Choices = [ u"合数大", u"合数小", u"合数单", u"合数双", wx.EmptyString ]
        self.m_comboBox4211 = wx.ComboBox( self, wx.ID_ANY, u"合数大", wx.DefaultPosition, wx.Size( 80,-1 ), m_comboBox4211Choices, 0 )
        bSizer411.Add( self.m_comboBox4211, 0, wx.ALL, 5 )
        
        self.m_textCtrl4311 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer411.Add( self.m_textCtrl4311, 0, wx.ALL, 5 )
        
        self.m_textCtrl4411 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer411.Add( self.m_textCtrl4411, 0, wx.ALL, 5 )
        
        self.m_textCtrl4511 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer411.Add( self.m_textCtrl4511, 0, wx.ALL, 5 )
        
        self.m_checkBox4611 = wx.CheckBox( self, wx.ID_ANY, u"启用", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer411.Add( self.m_checkBox4611, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer411, 1, wx.EXPAND, 5 )
        
        bSizer412 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4112 = wx.StaticText( self, wx.ID_ANY, u"13", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        self.m_staticText4112.Wrap( -1 )
        bSizer412.Add( self.m_staticText4112, 0, wx.ALL, 5 )
        
        m_comboBox4212Choices = [ u"合数大", u"合数小", u"合数单", u"合数双", wx.EmptyString ]
        self.m_comboBox4212 = wx.ComboBox( self, wx.ID_ANY, u"合数大", wx.DefaultPosition, wx.Size( 80,-1 ), m_comboBox4212Choices, 0 )
        bSizer412.Add( self.m_comboBox4212, 0, wx.ALL, 5 )
        
        self.m_textCtrl4312 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer412.Add( self.m_textCtrl4312, 0, wx.ALL, 5 )
        
        self.m_textCtrl4412 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer412.Add( self.m_textCtrl4412, 0, wx.ALL, 5 )
        
        self.m_textCtrl4512 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer412.Add( self.m_textCtrl4512, 0, wx.ALL, 5 )
        
        self.m_checkBox4612 = wx.CheckBox( self, wx.ID_ANY, u"启用", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer412.Add( self.m_checkBox4612, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer412, 1, wx.EXPAND, 5 )
        
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
    

