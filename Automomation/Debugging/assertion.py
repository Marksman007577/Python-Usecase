podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'

"""Here we’ve set podBayDoorStatus to 'open', so from now on, we fully
expect the value of this variable to be 'open'. In a program that uses this
variable, we might have written a lot of code under the assumption that
the value is 'open'—code that depends on its being 'open' in order to work
as we expect. So we add an assertion to make sure we’re right to assume
podBayDoorStatus
is 'open'. Here, we include the message 'The pod bay doors
need to be "open".' so it’ll be easy to see what’s wrong if the assertion fails.
Later, say we make the obvious mistake of assigning podBayDoorStatus
another value, but don’t notice it among many lines of code. The assertion
catches this mistake and clearly tells us what’s wrong.
In plain English, an assert statement says, “I assert that this condition
holds true, and if not, there is a bug somewhere in the program.” Unlike
exceptions, your code should not handle assert statements with try and
except; if an assert fails, your program should crash. By failing fast like this,
you shorten the time between the original cause of the bug and when you
first notice the bug. This will reduce the amount of code you will have to
check before finding the code that’s causing the bug.
Assertions are for programmer errors, not user errors. For errors that
can be recovered from (such as a file not being found or the user entering
invalid data), raise an exception instead of detecting it with an assert
statement."""


"""Disabling Assertions
Assertions can be disabled by passing the -O option when running Python.
This is good for when you have finished writing and testing your program
and don’t want it to be slowed down by performing sanity checks (although
most of the time assert statements do not cause a noticeable speed difference).
Assertions are for development, not the final product. By the time you
hand off your program to someone else to run, it should be free of bugs
and not require the sanity checks."""