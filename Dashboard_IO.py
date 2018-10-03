import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd


df = pd.read_csv('Insert target file path')

app = dash.Dash()


def encode_image(img_file):
    encoded = base64.b64encode(img_file, 'rb').read())
    return 'data:image/png;base64, {}'.format(encoded.decode())





app.layout = html.Div([
                    dcc.RangeSlider(id='range-slider',
                                    min = -10,          #    min value of slider
                                    max = 11,           #    max value of slider
                                    marks = {i: str(i) for i in range(-10,10)}, # build the length of the slider
                                    value = [-1,1]),    #    by passing two values we get two slider inputs
                    html.H1(id='outputid1')    # starting (placeholder) value

                    dcc.RadioItems(id='inputid1',
                                   options=[{'label': i,'value': i} for i in df['column_name1'].unique()]),
                    html.Div(id='outputid2'),   # Output division 1

                    html.Hr(),                  # Horizontal Row

                    dcc.RadioItems(id='inputid2'),
                                   options=[{'label': i, 'value': i} for i in df['column_name2'].unique()],
                                   value=str(df[0]),
                    html.Div(id='outputid3'),   # Output division 2
                    html.Img(id='imageid1', src='children', height=260)   # Output Image
                    ], style = {'fontFamily: helvetica', 'fontSize': 18}) # 'wrapper css'




#        Handles Slider input 1
#        We can handle evaluations within the return of the slider
@app.callback(Output('outputid1', 'children'),
               [Input('range-slider', 'value'))
def update_slider(value_list):
    return value_list[0] * value_list[1]



# Handles Radio input 2
@app.callback(Output('outputid2', 'children'),
              [Input('inputid1', 'value')])
def callback_a(value1):
    return 'you choose {}'.format(value1)


# Handles Radio input 3
@app.callback(Output('outputid3', 'children'),
              [Input('inputid2', 'value')])
def callback_b(value2):
    return 'you choose {}'.format(value2)
