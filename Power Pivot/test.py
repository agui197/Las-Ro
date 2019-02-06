# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 13:12:24 2019

@author: admin
"""

import dash
import dash_core_components as dcc
import dash_html_components as html

app =dash.Dash()
app.layout = html.Div(children=[
    html.H1('Dash tutorials'),
    dcc.Graph(id='example',
             figure={
                 'data':[
                     {'x':[1,2,3,4,5],'y':[6,6,7,3,4],'type':'line','name':'boats'},
                     {'x':[1,2,3,4,5],'y':[3,5,8,9,5],'type':'bar','name':'cars'},
                     
 
                 ],
                 'layout':'basic dash'
             })
])
if __name__=='__main__':
    app.run_server(debug=True)