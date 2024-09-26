# Created by parad at 9/17/2024
Feature: Test for Target sign in
  # Enter feature description here


  Scenario: User can sign in via side navigation menu
    Given Open Target main page
    When Go to Sign In
    Then Verify Sign In page


  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target main page
    When Go to Sign In
    When Store original window
    And Click on Target terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page is opened
    And Close current page
    And Return to original window