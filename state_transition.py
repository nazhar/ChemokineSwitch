import boolean2
from boolean2 import util, state, network
import os


def simulation( trans, rules ):
    "One simulation step will update the transition graph"

    # create the model
    print(rules)
    model = boolean2.Model ( text=rules, mode='sync')
    # generates all states, set limit to a value to keep only the first that many states
    # when limit is a number it will take the first that many initial states
    initializer = state.all_initial_states( model.nodes, limit=None )
     
    # the data is the inital data, the func is the initializer
    for data, initfunc in initializer:
        model.initialize(missing=initfunc)
        model.iterate(10)
        trans.add( model.states, times=range(10) )
        #print model.states 

def main():

    """This is the main code that runs the simulation many times"""
    for model_name in ['modelA', 'modelB', 'modelC', 'modelD', 'modelE']:
        with open('model_rules/' + model_name + '.txt', 'r') as file:
            rules = file.read()
        for injury in ['Moderate', 'Severe']:
            if injury == 'Moderate':
                rules = rules.replace("ISS_hi = True", "ISS_hi = False")
            else:
                rules = rules.replace("ISS_hi = False", "ISS_hi = True")

            modeltemp = boolean2.Model(text=rules, mode='sync')
            modeltemp.initialize()

            runname = 'model_output/Injury ' + injury + ' ' + model_name

            # this will hold the transition graph
            #trans = network.TransGraph( logfile=runname + '.log', verbose=True )
            # will run the simulation this many times. For sync updates 1 run is sufficient
            for num in range( 1 ):
                simulation ( trans, rules )

            # saves the transition graph into a gml file
            #trans.save( runname + '.gml' )
            trans.save(runname + '.gml')


main()
