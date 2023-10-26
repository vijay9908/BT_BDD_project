Feature: Filter Validations

    Background: 
        Given launch Chrome browser

    Scenario: Verify user is able to filter items using size filter
        When Navigate to shopping website
        And Poll data of all sizes from Website
        And Selecting the entered size XS and validating data
        And Validating combined filters of provided sizes S,M,ML,L,XL,XXL
        Then close the Chrome browser

    # Scenario: Verify results under S and M together and individual are correct
