
import sys
import boolean2
import numpy as np
import pandas as pd
from boolean2 import util
from boolean2 import Model
import os
import re


if not os.path.exists('model_output'):
    os.makedirs('model_output')

for model_name in ['modelA','modelB', 'modelC', 'modelD','modelE']:
    with open('model_rules/' + model_name + '.txt', 'r') as file:
        rules = file.read()
    df = pd.DataFrame()

    for injury in ['Moderate', 'Severe']:
        if injury == 'Moderate':
            rules = rules.replace("ISS_hi = True", "ISS_hi = False")
        else:
            rules = rules.replace("ISS_hi = False", "ISS_hi = True")

        coll  = util.Collector()
        iter =500
        seen = {}



        print model_name
        print rules

        for i in range(iter):
            model = boolean2.Model( text = rules, mode='sync')
            model.initialize()
            model.iterate( steps=20 )
            #print model.states

            # detect the cycles in the states
            size, index = model.detect_cycles()

            # fingerprint of the first state
            key = model.first.fp()
            
            # keep only the first 10 states out of the 20
            values = [ x.fp() for x in model.states[:10] ]

            # store the fingerprinted values for each initial state
            seen [ key ] = (index, size, values )
            nodes = model.nodes
            #print nodes
            states = model.states
            mydf = pd.DataFrame([[int(getattr(state, node)) for node in nodes] for state in states])
            mydf.columns = list(nodes)
            mydf['simID'] = i
            mydf['timepoint'] = range(21)
            mydf['injury'] = injury
            df = pd.concat([df, mydf], 0)
            coll.collect( states=states, nodes=nodes )
    df.to_csv('model_output/' + model_name  + '_sim.csv', index = False)
