# Problem Statement


An airline company needs you to implement a system to help book seats on flights. This airline company
has only one kind of plane with 20 rows, each row with a seat arrangement like so where ‘x’ represents
a seat:
| xx _ xxxx _ xx |
Seats are identified using a letter to indicate the row and a number to represent the position in the row.
The first row is identified as ‘A’ and the first seat in row A is ‘0’ and is thereby identified as ‘A0’.
Payment information is handled by another team and system, so we only need to focus on the
reservation of the seats themselves.

# Requirements

1. The state of reserved seats should be maintained in a file
1. A given seat cannot be reserved by more than one person
1. Once a person has a seat reservation they cannot be moved
1. If a customer cancels their reservation, the seat is available for reserving again
1. If a customer wants to reserve multiple seats together in the same row, we should be able to
accommodate that or tell the customer it’s not possible
1. Must be able to run in a Linux environment
1. Input must be accepted from CLI arguments specifically
1. Output must go to STDOUT


# Application

To solve the problem I built a functional command line application using Python and typer. Typer is a relatively young library
for creating powerful command line interface.


# Usage

To see available application commands use help: `python  -m flight_resy --help`

To book a flight use the command: `python  -m flight_resy book -s B2  -n 1`. You can see the description
for used flags by calling help

To cancel a flight use the command: `python  -m flight_resy cancel -s B2  -n 1`. You can see the description
for used flags by calling help


# Testing

To run the tests simply run the following command `python3.8  -m pytest tests`, it will run the tests
specified in the requirenment file
