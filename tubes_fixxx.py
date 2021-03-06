import pandas as pd

import bokeh
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs



from os.path import dirname, join

from linePlot import lineplot_tab 
from table import table_tab
from femalePlot import femaleplot_tab

world_population = pd.read_csv('archives/WorldPopulation.csv')
femaleperc = pd.read_csv('archives/population_female_percentage_long.csv')

tab1 = lineplot_tab(world_population)
tab2 = femaleplot_tab(femaleperc)
tab3 = table_tab(world_population)
tabs = Tabs(tabs = [tab1, tab2, tab3])


curdoc().add_root(tabs)
curdoc().title = "My test"
