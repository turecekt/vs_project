echo "LINT Flake8 output: "
python3 -m flake8 .
echo "Unit Test pytest output:  "
python3 -m pytest --doctest-modules --cov=. -cov-fail-under=75
pause

