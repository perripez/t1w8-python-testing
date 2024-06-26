# t1w8-python-testing

## Virtual Environments
- They help create isolated environments for your projects, ensuring each project has it own dependencies.

## Testing
- It allows us to confirm whether the application works as intended or not.
- It helps catch nugs early and helps us ensure that the code runs or behaves smoothly.

### Types of Testing
- Manual vs Automated:
    - Manual: when a person manually performs tasks, based on events.
    - Automated: programmed tests, also called scripts, to automatically perform tasks without human involvement.

- Unit testing: testing specific components/functions/methods of the program.
- Integration testing: testing the compatability with other modules or packages.
- Chaos testing: making a program break on purpose by disabling a function or feature to see how errors are handled.
- Stress testing: testing in high volume of data/inputs (depending on use-case).
- End to end/Acceptance testing: testing done towards the end of the project when it is almost complete to ensure it works effectively.

__Note: it's a great idea to organise your directory structure for miantenance and easy access__

### pytest

- Power and user-friendly testing framework
- Simple yet powerful.
- pytest follows the principal of 'assert'-ing that things are true in order to pass.
    - For a test to pass, assert  value must be true

- Reading test output: . means pass F means failes E exceptions happened

#### Exceptions
- Used to check what happens when things go wrong.
- How your program is handled when things go wrong.

### Parameterized tests
- Might want to test the same function with multiple inputs.
- Creates different text cases for all the different inputs provided.
- Make sure you initilise packages to use in other folders
