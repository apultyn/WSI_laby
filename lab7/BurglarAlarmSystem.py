from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

import sys
import argparse
import json


def print_CPD(list):
    for cpd in list:
        print(cpd)


def probability(network, dict):
    inference = VariableElimination(network)
    result = inference.query(
        variables=dict["variable"],
        evidence=dict["evidence"]
    )
    return result.values[dict["which"]] * 100


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("test_file")
    args = parser.parse_args(arguments[1:])
    dict = []

    with open(args.test_file, 'r') as file_handle:
        dict = json.load(file_handle)

    network = BayesianNetwork()
    network.add_nodes_from(['Burglary', 'Earthquake', 'Alarm',
                            'John', 'Mary', 'CallAnswered'])

    burglaryCPD = TabularCPD(
        variable="Burglary",
        variable_card=2,
        values=[
            [0.99],
            [0.01]
        ]
    )
    earthquakeCPD = TabularCPD(
        variable="Earthquake",
        variable_card=2,
        values=[
            [0.998],
            [0.002]
        ]
    )
    alarmCPD = TabularCPD(
        variable="Alarm",
        variable_card=2,
        values=[
            [0.999, 0.71, 0.06, 0.05],
            [0.001, 0.29, 0.94, 0.95]],
        evidence=["Burglary", "Earthquake"],
        evidence_card=[2, 2]
    )
    johnCallsCPD = TabularCPD(
        variable="John",
        variable_card=2,
        values=[
            [0.8, 0.01],
            [0.2, 0.99]
        ],
        evidence=["Alarm"],
        evidence_card=[2]
    )
    maryCallsCPD = TabularCPD(
        variable="Mary",
        variable_card=2,
        values=[
            [0.99, 0.3],
            [0.01, 0.7]
        ],
        evidence=["Alarm"],
        evidence_card=[2]
    )
    CallAnsweredCPD = TabularCPD(
        variable="CallAnswered",
        variable_card=2,
        values=[
            [1, 0.4, 0.4, 0.05],
            [0, 0.6, 0.6, 0.95]
        ],
        evidence=["John", "Mary"],
        evidence_card=[2, 2]
    )

    print_CPD([
        burglaryCPD, earthquakeCPD,
        alarmCPD, johnCallsCPD, maryCallsCPD, CallAnsweredCPD
    ])

    network.add_cpds(burglaryCPD, earthquakeCPD,
                     alarmCPD, johnCallsCPD, maryCallsCPD, CallAnsweredCPD)
    network.add_edges_from([
        ('Burglary', 'Alarm'),
        ('Earthquake', 'Alarm'),
        ('Alarm', 'John'),
        ('Alarm', 'Mary'),
        ('John', 'CallAnswered'),
        ('Mary', 'CallAnswered')
    ])

    assert network.check_model(), "The model has inconsistencies."

    with open("results.txt", 'w') as file_handle:
        for test in dict:
            file_handle.write(
                f"{test['name']}: {probability(network, test):.2f}%\n"
            )


if __name__ == "__main__":
    main(sys.argv)
