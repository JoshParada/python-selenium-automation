# Created by parad at 9/16/2024
Feature: Test for Target empty cart and sign in
  # Enter feature description here

  Scenario: User can go to cart
    Given Open Target main page
    When Go to Cart
    Then Verify cart is empty


  Scenario: User can sign in via side navigation menu
    Given Open Target main page
    When Go to Sign In
    Then Verify Sign In page