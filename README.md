# Testing - ResX

Notes from testing the ResX_1.4.0.apk file

## Bugs

### Registration Error

If the user tries to register and enters a correct phone number the app will save that registration attempt. No matter what the user does when he tries to register or login the app will offer them the choice to return to only the first registration attempt.

### Incorrect Groups

There is an issue with the way the reservation cards are displayed. In the Home View the Reservation Elements are incorrectly grouped. An element inspector reveals that the last group element which represents a reservation is grouped up with the recently claimed reservations and Show/Hide toggle button instead of being grouped individually like it's suppose to be. This may cause unexpected behavior when more reservations are displayed.

### Default city in alert bug

In the alert view the "Choose your city" option alternates between defaulting to New York and Miami seemingly at random.

### Deleting alerts sometimes produces a bug

After creating and trying to immediately delete an alert, the alert is not deleted and an error message appears "Something Went Wrong". Could not recognize any pattern.

### "Deleted" alert sometimes remains

After an alert is successfully deleted, upon exiting and reentering the alerts screen the alert remains.

## Tests

The tests were created using the Appium API and PyTest framework. **Previous test results can be found in the reports folder**. To run your own tests add a new file named "test_{...}.py" {...} being the name of the test and write your test function in the file. To run the tests, simply run the ``pytest`` command in the terminal in your root folder. After every test is done the results will be saved in the root of the project under the name "report.html". To save the report move it into the reports folder and change its name, otherwise it will be rewritten.