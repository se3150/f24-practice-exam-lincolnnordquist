Feature: calculate the area of a triangle
    As an aspiring mathematician
    I should be able to calculate the area of a triangle
    So that I can chat with my math friends like a pro

Scenario: I can calculate the area of a triangle
    Given I open the url "https://byjus.com/herons-calculator/"
    When I input "8" into the search field with id "a"
    When I input "15" into the search field with id "b"
    When I input "17" into the search field with id "c"
    And I click the element with type "button"
    Then I expect that the element with class "oOutp" contains the text "60"