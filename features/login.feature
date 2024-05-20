Feature: Login Page
  Scenario: Check that URL is correct
    Given I am on the login page
    Then The URL is  "https://www.fonduri-structurale.ro/contul-meu/inregistrare"

  Scenario: Log in with unregistered email
    Given I am on the login page
    When I enter "mvisovan@gmail.com" in the email input
    When I enter "123456" in the password input
    When I click login button
    Then I should see the red message "Ești înregistrat?"


#testele se ruleaza din terminal cu behave