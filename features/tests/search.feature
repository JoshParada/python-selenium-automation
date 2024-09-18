# Created by parad at 9/17/2024
Feature: Test for Target search functionality for multiple products

  Scenario: User can search for coffee
    Given Open Target main page
    When Search for plates
    Then Verify that results match plates


  Scenario: User can search for tea
    Given Open Target main page
    When Search for cups
    Then Verify that results match cups


#  Scenario Outline: User can search for product
#    Given Open target main page
#    When Search for <search_word>
#    Then Verify that results match <search_result>
#    Examples:
#    |search_word  |search_result |
#    |coffee       |coffee        |
#    |tea          |tea           |
#    |mug          |mug           |
#    |sugar        |sugar         |