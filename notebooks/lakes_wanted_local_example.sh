#!/usr/bin/env bash

for i in SU ER ON HU MI
    do
    python3 ./lake_wanted_timeseries.py "$i"
    done 