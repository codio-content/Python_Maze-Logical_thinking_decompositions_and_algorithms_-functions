## Defining our function
To define a function called `initialise()`, we simply create the following

```python
def initialise():
  instructions
  within 
  the
  code 
  block
```

## Pass

If your functions does not have any instructions in it, we need to tell Python to pass over it like this otherwise Python will give you an error

```python
def initialise():
  pass
```

## Execution
When your code executes, it will not actually execute the contents of `initialise()` until it is explicitly called.

Comment out the `initialise()` line like this

```python
# initialise()
```

Then reload the game.

You will see that nothing happens other than the empty maze being created. This illustrates how the `initialise()` function only executes when it gets called.
