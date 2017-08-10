# round-robin
This module makes round-robin strings.

## Usage
### Installation
  This module has no installer yet, so you can install only yourself.
### Specification
#### Constructor Arguments
| name               | type | description                                                   |
| ------------------ |:----:| --------------------------------------------------------------|
| any_characters     | list | This list consolidate to character_list.                      |
| use_all            | bool | If it has True,  character_list has all aphabets and numbers. |
| use_aphabets       | bool | If it has True,  character_list has all aphabets.             |
| use_small_aphabets | bool | If it has True, character_list has smaller aphabets.          |
| use_large_aphabets | bool | If it has True, character_list has larger aphabets.           |
| use_numbers        | bool | If it has True, character_list has all numbers.               |


### Example
This program continue getting round_robin strings from RoundRobin.next() and printing them.

  ```python
  import round_robin
  import time
  
  roundrobin = round_robin.RoundRobin(use_all=True)
  
  for pattern in roundrobin.next():
    print(pattern)
    time.sleep(0.1)
  ```
