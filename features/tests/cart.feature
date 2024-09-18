# Created by parad at 9/17/2024
Feature: Test for Target empty cart and add item
  # Enter feature description here

  Scenario: User can go to cart
    Given Open Target main page
    When Go to Cart
    Then Verify cart is empty


  Scenario: User can add item to cart
    Given Open Target main page
    When Search for paper towels
    When Add first item to cart
    When Go to Cart
    Then Verify item is in cart