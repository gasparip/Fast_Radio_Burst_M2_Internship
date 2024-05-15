#!/bin/bash
echo 'psredit /databf2/nenufar-pulsar/{ES,LT}05/*/*/*.fits | grep  "Source name" | colrm 1 67 | sort | uniq -c' 
psredit /databf2/nenufar-pulsar/{ES,LT}05/*/*/*.fits | grep  "Source name" | colrm 1 67 | sort | uniq -c
exit 1

