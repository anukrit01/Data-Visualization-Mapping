from bokeh.plotting import output_file, show, figure
import pandas

dataset = pandas.read_excel('https://pythonhow.com/verlegenhuken.xlsx', sheet_name=0)
dataset['Temperature'] = dataset['Temperature']/10
dataset['Pressure'] = dataset['Pressure']/10

p = figure(plot_width= 500, plot_height= 400)

p.title.text = "Temperature and Air Pressure"
p.title.text_color = "Red"
p.title.text_font = "ariel"
p.title.text_font_style = "bold"
p.xaxis.axis_label = "Temperature (C)"
p.yaxis.axis_label = "Pressure (hPa)"

p.circle(dataset["Temperature"], dataset["Pressure"], size= 0.1)
output_file('Weather.html')
show(p)