#!/bin/sh
coverage run --source topologyvalidator -m unittest discover
coverage report 
coverage html