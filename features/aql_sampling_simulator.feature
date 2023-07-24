Feature: verify acceptable quality limit

  Scenario: run a quantity with inspection level
     Given we are on the AQL web site
      When we complete all fields of AQL Sampling Simulator
      Then behave show all value points
