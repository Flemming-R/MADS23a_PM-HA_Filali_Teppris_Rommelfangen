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
from typing import Literal

def load_data(logname: Literal['domestic', 'international', 'nonanomaly_Domestic', 'nonanomaly_International']):
    """Load logdata from path Data/"""
    log_path = f'Data/{logname.title()}Declarations.xes'
    log = pm4py.read_xes(log_path)
    return log