# mytodo

This CLI Application was built using Python and after installation will allow you to add, remove, delete, complete and view
your To-Do list in an extremely simple way. 

## Getting Started

### Prerequisites

You must have Python 3 and the Python module "pip" installed on your machine before setting up.

### Installing

To install this CLI onto your machine, download the zip of this repository and navigate into this directory in the terminal.
Then you must run the shell script with administrative privliges.
EX: sudo ./install.sh

## Usage:
mytodo will begin before all arguments.

-v : (View) Will print to the console all current tasks you have and their assigned numbers.

-a  <"My task">: (Add) Will add a task to your task list [be sure that you put your task in quotations].

-a -mit <"My task">: (Add MIT) Will add a task to your MIT (Most Important Take) list [Task in Quotations].

-c <task #> : (Complete) Will set a task marked for completion.

-d <task #>   : (Delete) Will delete a task and reorder the list.

-d -all       : (Delete All) Will delete EVERY task from all lists.

-d -mit   : (Delete All MIT) Will delete EVERY task from the MIT list.

-d -reg    : (Delete All Regular) Will delete EVERY task from the Regular list.

## Built With

* [Python](https://github.com/python/cpython) - The programming language used

## Authors

* **Colby Allen**
