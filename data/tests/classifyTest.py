import pytest
import sys

sys.path.insert(1, "./data/user_classification/")
import classify
# Unit test for findIssueAvg() function in classify.py
def test_findIssueAvg():
    responses = [1, 1.5, 2, 1, 1, 1, 2, 2, 2, 1, 1.2, 1.4, 2, 1.5, 1.75, 1.5, 1.25, 1, 1, 1, 1, 2, 2, 2, 1.5, 1.5, 1.5, 1.1, 1.0, 1.2, 1.5, 1.6, 1.7, 2, 2, 2, 1.2, 1.4, 1.6, 1.5, 1, 2]
    assert classify.findIssueAvg(responses) == [1.5, 1.0, 2.0, 1.2, 1.75, 1.25, 1.0, 2.0, 1.5, 1.1, 1.6, 2.0, 1.4, 1.5 ]

def test_findIssueAvg2():
    responses = [2, 2, 2, 1, 1.2, 1.4, 2, 2, 2, 1, 1.2, 1.4, 2, 1, 1.5, 1.5, 1.25, 1, 1, 1, 1, 2, 2, 2, 1.5, 1.5, 1.5, 1.1, 1.0, 1.2, 1.5, 1.6, 1.7, 2, 2, 2, 1.2, 1.4, 1.6, 1.5, 1, 2]
    print (len(responses))
    assert classify.findIssueAvg(responses) == [2, 1.2, 2.0, 1.2, 1.5, 1.25, 1.0, 2.0, 1.5, 1.1, 1.6, 2.0, 1.4, 1.5 ]

# Unit Test for distance()
def test_distance():
    responses = [1, 1.5, 2, 1, 1, 1, 2, 2, 2, 1, 1.2, 1.4, 2, 1.5, 1.75, 1.5, 1.25, 1, 1, 1, 1, 2, 2, 2, 1.5, 1.5, 1.5, 1.1, 1.0, 1.2, 1.5, 1.6, 1.7, 2, 2, 2, 1.2, 1.4, 1.6, 1.5, 1, 2]
    responses = classify.findIssueAvg(responses)
    targetJustice = [1, 1.5, 2, 2, 1.4, 1.9, 1.5, 1, 2, 1.5, 1, 2, 1.3, 1.4]
    assert classify.distance(responses, targetJustice) == 0.266

def test_distance2():
    responses = [2, 2, 2, 1, 1.2, 1.4, 2, 2, 2, 1, 1.2, 1.4, 2, 1, 1.5, 1.5, 1.25, 1, 1, 1, 1, 2, 2, 2, 1.5, 1.5, 1.5, 1.1, 1.0, 1.2, 1.5, 1.6, 1.7, 2, 2, 2, 1.2, 1.4, 1.6, 1.5, 1, 2]
    responses = classify.findIssueAvg(responses)
    targetJustice = [1, 1.5, 2, 2, 1.4, 1.9, 1.5, 1, 2, 1.5, 1, 2, 1.3, 1.4]
    assert classify.distance(responses, targetJustice) == 0.3

def test_findClosestJustice():
    example_justice = [[1, 1.5, 2, 2, 1.4, 1.9, 1.5, 1, 2, 1.5, 1, 2, 1.3, 1.4],[1, 1.5, 2, 2, 1.4, 1.9, 1.5, 1, 2, 2, 2, 1, 1.3, 1.4]]
    responses = [1, 1.5, 2, 1, 1, 1, 2, 2, 2, 1, 1.2, 1.4, 2, 1.5, 1.75, 1.5, 1.25, 1, 1, 1, 1, 2, 2, 2, 1.5, 1.5, 1.5, 1.1, 1.0, 1.2, 1.5, 1.6, 1.7, 2, 2, 2, 1.2, 1.4, 1.6, 1.5, 1, 2]
    responses = classify.findIssueAvg(responses)
    judgeId = classify.findClosestJustice(responses, example_justice)
    assert (judgeId == 78)


def test_findClosestJustice2():
    example_justice = [[1, 1.5, 2, 2, 1.4, 1.9, 1.5, 1, 2, 1.5, 1, 2, 1.3, 1.4],[1, 1.5, 2, 2, 1.4, 1.9, 1.5, 1, 2, 2, 2, 1, 1.3, 1.4]]
    responses = [1, 1.5, 2, 2, 1.4, 1.9, 1.5, 1, 2, 2, 2, 1, 1.3, 1.4]
    judgeId = classify.findClosestJustice(responses, example_justice)
    assert (judgeId == 79)
