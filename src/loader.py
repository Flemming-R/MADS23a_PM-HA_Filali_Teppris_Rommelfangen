import pm4py
import io
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.visualization.bpmn import visualizer as bpmn_vis


log_domestic = xes_importer.apply('Data/DomesticDeclarations.xes')
log_international = xes_importer.apply('Data/InternationalDeclarations.xes')
df_domestic = pm4py.convert_to_dataframe(log_domestic)
df_international = pm4py.convert_to_dataframe(log_international)
