#!/bin/bash

parallel ./check.sh < $1 >> $2
