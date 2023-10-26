Feature: add items to cart

    Background: 
        Given launch Chrome browser

    Scenario: Verify items are listed in cart in the order as added to cart with price
        When Navigate to shopping Homepage
        And Add random 4 items into cart with free shipping and one without
        And Verify cart post adding items
        Then close the Chrome browser