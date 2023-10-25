Feature: Filter Validation

    Background: 
        Given launch Chrome browser

    Scenario: Verify user is able to filter items using size filter
        When Navigate to shopping website
        And selecting the size XS to XXL
        Then close the Chrome browser

    # Scenario: Verify results under S and M together and individual are correct
