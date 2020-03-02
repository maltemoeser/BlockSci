#!/bin/bash
pytest --benchmark-compare --benchmark-compare-fail=mean:5% --benchmark-sort=name --benchmark-group-by=name --btc
