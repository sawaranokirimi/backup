#coding: utf-8
import pandas as pd
import os
import wx
import run_all
import analyze
import draw_all
import making_map
import matplotlib.pyplot as plt
import mvfiles
import auto
#import giff

class UI():
    def __init__(self):
        self.frame = wx.Frame(None, wx.ID_ANY, u"Ikeda&Murotaの空間周波数分析アプリver.K", size=(400,300))
        self.frame.Show()
        
    def click_button_2(self, event):
        self.frame.SetStatusText(u"左から右へと線を引いて")
        run_all.main1()
        self.frame.SetStatusText(u"解析結果を出力します")
        analyze.main1()
        self.frame.SetStatusText("")
    
    def click_button_3(self, event):
        self.frame.SetStatusText("作図中です")
        draw_all.main1()
        plt.close('all')
        plt.show()
        self.frame.SetStatusText("作図が完了しました")
        
    def click_button_4(self, event):
        self.frame.SetStatusText("フロッピーのマークが保存です")
        making_map.main3()
        self.frame.SetStatusText("")

    def click_button_B1(self, event):
        text = self.text_5.GetValue()
        mvfiles.Boukennosyo().hozon(text)
        self.frame.SetStatusText("保存しました")

    def click_button_C1(self, event):
        self.frame.SetStatusText("繰り返し計算の範囲を確認")
        df = pd.read_csv('data_lt_rb.csv', index_col=0)
        lt= [df.ix[0,0], df.ix[0,1]]
        rb= [df.ix[1,0], df.ix[1,1]]

        values = []
        for tc in self.tcs:
            print tc.GetValue()
            values.append(tc.GetValue())
        print values
        df2 = pd.DataFrame(values).T
        df2.columns = ('slide_l', 'slide_n', 'rotate_theta', 'rotate_n',\
              'zoom_p', 'zoom_n')         
        df2.to_csv('.roop_parameter.csv', index=None)
        lt_rb = auto.automation(lt, rb, slide_l=float(values[0]), slide_n=int(values[1]),\
                       rotate_theta=float(values[2]), rotate_n=int(values[3]),\
                       zoom_p=float(values[4]), zoom_n=int(values[5]))
        print lt_rb
        making_map.for_auto(lt_rb, kaiseki=False)

    def click_button_C2(self, event):
        self.frame.SetStatusText("長時間かかります")
        df = pd.read_csv('data_lt_rb.csv', index_col=0)
        lt= [df.ix[0,0], df.ix[0,1]]
        rb= [df.ix[1,0], df.ix[1,1]]

        values = []
        for tc in self.tcs:
            print tc.GetValue()
            values.append(tc.GetValue())
        print values
        df2 = pd.DataFrame(values).T
        df2.columns = ('slide_l', 'slide_n', 'rotate_theta', 'rotate_n',\
              'zoom_p', 'zoom_n')         
        df2.to_csv('.roop_parameter.csv', index=None)
        lt_rb = auto.automation(lt, rb, slide_l=float(values[0]), slide_n=int(values[1]),\
                       rotate_theta=float(values[2]), rotate_n=int(values[3]),\
                       zoom_p=float(values[4]), zoom_n=int(values[5]))
        auto.roop(lt_rb).to_csv('data_rooped.csv')

        os.system('mplayer .oda.mp4')

        temp = pd.read_csv('data_rooped.csv', index_col=0)
        making_map.for_auto(temp, kaiseki=True)
        self.frame.SetStatusText("")
        run_all.max_of_rooped()
        analyze.main1()





    def make_window(self):
        frame = self.frame
        frame.CreateStatusBar()
        notebook = wx.Notebook(frame, wx.ID_ANY)

        panel = wx.Panel(notebook, wx.ID_ANY)
        panelB = wx.Panel(notebook, wx.ID_ANY)
        panelC = wx.Panel(notebook, wx.ID_ANY)
        panel.SetBackgroundColour("#AFAFAF")
        panelB.SetBackgroundColour("#AFAFAF")
        panelC.SetBackgroundColour("#AFAFAF")

        #panelA
        button_2 = wx.Button(panel, wx.ID_ANY, u"アナライズ")
        button_3 = wx.Button(panel, wx.ID_ANY, u"作図(パターン図)")
        button_4 = wx.Button(panel, wx.ID_ANY, u"作図(分析領域図)")

        button_2.Bind(wx.EVT_BUTTON, self.click_button_2)
        button_3.Bind(wx.EVT_BUTTON, self.click_button_3)
        button_4.Bind(wx.EVT_BUTTON, self.click_button_4)

        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(button_2, proportion=1)
        layout.Add(button_3, proportion=1)
        layout.Add(button_4, proportion=1)
        panel.SetSizer(layout)

        #panelB
        text_1 = wx.StaticText(panelB, wx.ID_ANY, '前回のフォルダ名')
        text_1.SetForegroundColour("#0000FF")
        text_2 = wx.StaticText(panelB, wx.ID_ANY, mvfiles.Boukennosyo().ex_filename())
        text_3 = wx.StaticText(panelB, wx.ID_ANY, '')
        text_4 = wx.StaticText(panelB, wx.ID_ANY, '新しく作るフォルダ名')
        text_4.SetForegroundColour("#0000FF")
        element_array = [mvfiles.Boukennosyo().new_filename(), 'usa_pop-', 'south_germany-pop-', 'temp']
        text_5 = wx.ComboBox(panelB, wx.ID_ANY, u"選んでください", choices=element_array,\
                            style=wx.CB_DROPDOWN)
        self.text_5 = text_5
        button_B1 = wx.Button(panelB, wx.ID_ANY, "保存")
        
        button_B1.Bind(wx.EVT_BUTTON, self.click_button_B1)
        
        layoutB = wx.BoxSizer(wx.VERTICAL)
        layoutB.Add(text_1)
        layoutB.Add(text_2)
        layoutB.Add(text_3)
        layoutB.Add(text_4)
        layoutB.Add(text_5, flag=wx.GROW)
        layoutB.Add(button_B1)
        panelB.SetSizer(layoutB)

        #panelC
        df = pd.read_csv('.roop_parameter.csv').values[0]
        df_name = ('slide_l', 'slide_n', 'rotate_theta', 'rotate_n',\
              'zoom_p', 'zoom_n')         

        panelC_1 = wx.Panel(panelC, wx.ID_ANY)
        panelC_2 = wx.Panel(panelC, wx.ID_ANY)
        
        #C1
        layout_C_1 = wx.GridSizer(6, 2)
        tc0 = wx.TextCtrl(panelC_1, wx.ID_ANY, str(df[0]))
        tc1 = wx.TextCtrl(panelC_1, wx.ID_ANY, str(df[1]))
        tc2 = wx.TextCtrl(panelC_1, wx.ID_ANY, str(df[2]))
        tc3 = wx.TextCtrl(panelC_1, wx.ID_ANY, str(df[3]))
        tc4 = wx.TextCtrl(panelC_1, wx.ID_ANY, str(df[4]))
        tc5 = wx.TextCtrl(panelC_1, wx.ID_ANY, str(df[5]))
        self.tcs = [tc0, tc1, tc2, tc3, tc4, tc5]
        for x, name, tc in zip(df, df_name, self.tcs):
            temp_name = wx.StaticText(panelC_1, wx.ID_ANY, name)
            layout_C_1.Add(temp_name)
            layout_C_1.Add(tc)

        panelC_1.SetSizer(layout_C_1)

        #C2
        layout_C_2 = wx.BoxSizer(wx.VERTICAL)
        button_C_2A = wx.Button(panelC_2, wx.ID_ANY, u"範囲の確認")
        button_C_2A.Bind(wx.EVT_BUTTON, self.click_button_C1)
        button_C_2B = wx.Button(panelC_2, wx.ID_ANY, u"分析！！")
        button_C_2B.Bind(wx.EVT_BUTTON, self.click_button_C2)
        font = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        button_C_2A.SetFont(font)
        button_C_2B.SetFont(font)
        button_C_2B.SetForegroundColour("#FF0000")
        layout_C_2.Add(button_C_2A)
        layout_C_2.Add(button_C_2B)

        panelC_2.SetSizer(layout_C_2)
        
        layout_C = wx.BoxSizer(wx.HORIZONTAL)
        layout_C.Add(panelC_1, proportion=2)
        layout_C.Add(panelC_2, proportion=1)
        panelC.SetSizer(layout_C)


        notebook.InsertPage(0, panel, u"くじ引き") 
        notebook.InsertPage(1, panelC, u"オートくじ引き")
        notebook.InsertPage(2, panelB, u"セーブ")




def main1():
    app = wx.App(False)
    ui = UI()
    ui.make_window()
    app.MainLoop()



if __name__ == '__main__':
    main1()
