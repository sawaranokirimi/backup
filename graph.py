#coding: utf-8
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import seaborn as sb




class Graph():
    def __init__(self, fname):
        self.df = pd.read_csv(fname, encoding='utf-8', index_col='Unnamed: 0')
        py.sign_in('sawaranokirimi', '20g7wciegi')

    def columns(self):
        return ['uniform', 'm=3', 'm=4', 'm=9', 'm=12',\
                'm=27(Ⅰ)', 'm=27(Ⅱ)', 'm=27(Ⅲ)',\
                'm=36(Ⅰ)', 'm=36(Ⅱ)', \
                'm=81(Ⅰ)', 'm=81(Ⅱ)', 'm=81(Ⅲ)', 'm=81(Ⅳ)', 'm=81(Ⅴ)', 'm=81(Ⅵ)',\
                'm=108(Ⅰ)', 'm=108(Ⅱ)', 'm=108(Ⅲ)', 'm=108(Ⅳ)',\
                'm=108(Ⅴ)', 'm=108(Ⅵ)', \
                'm=324(Ⅰ)', 'm=324(Ⅱ)', 'm=324(Ⅲ)', 'm=324(Ⅳ)', 'm=324(Ⅴ)', 'm=324(Ⅵ)',\
                'm=324(Ⅶ)', 'm=324(Ⅷ)', 'm=324(Ⅸ)', 'm=324(X)', 'm=324(XⅠ)', 'm=324(XⅡ)',\
                'm=324(XⅢ)', 'm=324(XⅣ)', 'm=324(XⅤ)']
        
    def get_layout(self):      
        return go.Layout(title='',
                         width=800,
                         bargroupgap=0.3,
                         margin=dict(r=80, l=80),
                         yaxis=dict(title='power spectra',
                                    exponentformat='power',
                                    showexponent='last'
                                   ), 
                         xaxis=dict(tickangle=60,
                                    ticks='outside',
                                    tickwidth=2,
                                    ticklen=5,
                                    tickfont=dict(color='rgb(0,0,0)')
                                   ) 
                        )


    def get_bar(self):
        data = go.Bar(x=self.columns(),
                      y=self.df['norm'],
                      marker=dict(color='rgb(200,200,200)', line=dict(width=2))
                     )
        return data

    def figure(self):
        data = [self.get_bar()]
        layout = self.get_layout()
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='basic-bar')
        return fig

    def showfig(self):
        py.image.save_as(self.figure(), filename='figure_norm.pdf')


def main1():
    inputfile = 'norm.csv'
    graph = Graph(fname=inputfile)
    graph.showfig()



if __name__ == '__main__':
    main1()
