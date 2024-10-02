# Created by parad at 9/17/2024
Feature: Test for Target search functionality for multiple products

  Scenario: User can search for plates
    Given Open Target main page
    When Search for plates
    Then Verify that results match plates
    Then Verify product coffee in URL


  Scenario: User can search for cups
    Given Open Target main page
    When Search for cups
    Then Verify that results match cups
    Then Verify product coffee in URL


  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image


  Scenario: User can see favorites tooltip for search results
    Given Open Target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown


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